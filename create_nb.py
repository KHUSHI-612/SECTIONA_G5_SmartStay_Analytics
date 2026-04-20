import json

markdown_source = [
    "# Data Cleaning: Column Filtration\n",
    "In this step, we drop irrelevant and unidentifiable columns from the raw dataset based on our 3-way analytical perspective:\n",
    "1. Business Setup\n",
    "2. User Perspective\n",
    "3. Airbnb Growth\n",
    "\n",
    "The columns dropped include scraping metadata, internal URLs/IDs, completely null location features, mathematically redundant host fields, and overly granular availability parameters."
]

code_source = [
    "import pandas as pd\n",
    "\n",
    "# Load the raw dataset\n",
    "file_path = '../data/raw/airbnb_listing.csv'\n",
    "print(f\"Reading {file_path}...\")\n",
    "df = pd.read_csv(file_path, low_memory=False)\n",
    "\n",
    "# List of irrelevant/unidentifiable columns identified based on 3-way analysis\n",
    "cols_to_drop = [\n",
    "    # Scraping/Metadata\n",
    "    'scrape_id', 'last_scraped', 'source', 'calendar_updated', 'calendar_last_scraped',\n",
    "    # Identifiers & URLs\n",
    "    'id', 'listing_url', 'host_id', 'host_url',\n",
    "    # Overly-granular Booking Rules\n",
    "    'minimum_minimum_nights', 'maximum_minimum_nights', 'minimum_maximum_nights', 'maximum_maximum_nights',\n",
    "    'minimum_nights_avg_ntm', 'maximum_nights_avg_ntm',\n",
    "    # Missing / Redundant Geography\n",
    "    'neighbourhood_group_cleansed', 'host_neighbourhood', 'neighbourhood',\n",
    "    # Redundant Calculated Host Listings\n",
    "    'calculated_host_listings_count', 'calculated_host_listings_count_entire_homes',\n",
    "    'calculated_host_listings_count_private_rooms', 'calculated_host_listings_count_shared_rooms',\n",
    "    # Legal/Other\n",
    "    'license'\n",
    "]\n",
    "\n",
    "# Note: Image URLs like 'picture_url', 'host_thumbnail_url', and 'host_picture_url' \n",
    "# were already dropped manually, but we include them here for completeness \n",
    "# in case the script is run on a fresh raw dataset.\n",
    "image_urls = ['picture_url', 'host_thumbnail_url', 'host_picture_url']\n",
    "cols_to_drop.extend(image_urls)\n",
    "\n",
    "initial_cols = len(df.columns)\n",
    "# Drop columns that exist in the dataframe to prevent KeyError\n",
    "cols_actually_dropped = [col for col in cols_to_drop if col in df.columns]\n",
    "df.drop(columns=cols_actually_dropped, inplace=True)\n",
    "final_cols = len(df.columns)\n",
    "\n",
    "print(f\"Dropped {len(cols_actually_dropped)} columns.\")\n",
    "print(f\"Initial columns: {initial_cols}, Final columns: {final_cols}\")\n",
    "\n",
    "# Overwrite the raw dataset or save to interim folder\n",
    "save_path = '../data/raw/airbnb_listing.csv'\n",
    "df.to_csv(save_path, index=False)\n",
    "print(f\"Cleaned dataset saved back to {save_path}\")"
]

notebook = {
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": markdown_source
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "metadata": {},
   "outputs": [],
   "source": code_source
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}

with open('/Users/manangilhotra010/Desktop/SECTIONA_G5_SmartStay_Analytics/notebooks/02_cleaning.ipynb', 'w') as f:
    json.dump(notebook, f, indent=1)

print("Notebook generated directly via json block!")
