import pandas as pd
import numpy as np
import os

def run_etl(raw_path='data/raw/airbnb_listing.csv', processed_path='data/processed/cleaned_airbnb.csv'):
    """
    This is our main engine for cleaning data. 
    It takes the messy raw file and turns it into a clean CSV for our analysis.
    """
    print(f"🚀 Starting the SmartStay ETL Pipeline...")
    
    if not os.path.exists(raw_path):
        print(f"⚠️ Whoops! We couldn't find the raw data at {raw_path}. Make sure it's there!")
        return

    # Loading up the data
    print(f"📂 Loading data from {raw_path}...")
    df = pd.read_csv(raw_path, low_memory=False)
    
    # 1. Cleaning up the rows
    # If a listing doesn't have a price, it's not very useful for our business study, so we'll drop it.
    df = df.dropna(subset=['price'])
    
    # 2. Fixing symbols ($, %)
    # We need to strip '$', ',', and '%' so we can actually do math.
    if 'price' in df.columns:
        df['price'] = df['price'].astype(str).str.replace(r'[\$,]', '', regex=True)
    
    for col in ['host_acceptance_rate', 'host_response_rate']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.replace('%', '', regex=False)
    
    # 3. Force numeric types
    cols_to_force = [
        "price", "accommodates", "bedrooms", "beds", "bathrooms", 
        "minimum_nights", "availability_365", "number_of_reviews", 
        "review_scores_rating", "host_acceptance_rate", "reviews_per_month"
    ]
    for col in cols_to_force:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # 4. Filling in the gaps (Numeric)
    # For missing numbers, we'll use the median value.
    numeric_cols = df.select_dtypes(include=['number']).columns
    for col in numeric_cols:
        if df[col].isnull().any():
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            
    # 5. Filling in the gaps (Categorical)
    # If we don't know the value, we'll just call it 'Unknown'.
    categorical_cols = df.select_dtypes(include=['object', 'string']).columns
    for col in categorical_cols:
        if df[col].isnull().any():
            df[col] = df[col].fillna('Unknown')

    # 5. Dropping the stuff we don't need
    # There are a lot of columns that are just for the website (like URLs) or internal IDs.
    # We are cutting those out to keep our file small and fast.
    cols_to_drop = [
        'scrape_id', 'last_scraped', 'source', 'calendar_updated', 'calendar_last_scraped',
        'id', 'listing_url', 'host_url', 'picture_url', 'host_thumbnail_url', 
        'host_picture_url', 'minimum_minimum_nights', 'maximum_minimum_nights',
        'minimum_maximum_nights', 'maximum_maximum_nights', 'neighbourhood_group_cleansed',
        'host_neighbourhood', 'neighbourhood', 'host_has_profile_pic', 'host_verifications',
        'host_name', 'host_about', 'host_location', 'description', 'neighborhood_overview',
        'first_review', 'last_review', 'bathrooms_text', 'calendar_last_scraped'
    ]
    df = df.drop(columns=[c for c in cols_to_drop if c in df.columns])
 
    # 6. Final Polish
    # We want things like 'Superhost' to be simple 0 or 1 so our models can read them easily.
    binary_map = {'t': 1, 'f': 0, 'Unknown': 0}
    for col in ['host_is_superhost', 'instant_bookable', 'host_identity_verified']:
        if col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].map(binary_map).fillna(0)
    
    # Make sure the output folder exists
    os.makedirs(os.path.dirname(processed_path), exist_ok=True)
    
    # Save the final result
    df.to_csv(processed_path, index=False)
    print(f"✅ All done! We now have {df.shape[0]} clean rows and {df.shape[1]} columns.")
    print(f"📁 You can find the clean data at: {processed_path}")

if __name__ == "__main__":
    run_etl()
