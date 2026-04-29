# SmartStay Analytics: Unlocking the Albany Airbnb Market

Hey there! Welcome to the **SmartStay Analytics** project. We are a team of students (Section A, Group 5) who spent the last few weeks diving deep into the Airbnb ecosystem of Albany, NY. 

Our goal was simple but ambitious: instead of just looking at numbers, we wanted to build a toolkit that actually helps people make decisions. Whether you're an investor looking to buy your next rental, a guest wondering what makes a "good" stay, or just curious about how Airbnb is growing in our city, we've got you covered.

### What are we trying to solve?
*   **For the Business-Minded:** We identify which neighborhoods are the "gold mines" and which property types actually bring in the most cash.
*   **For the Guests:** We look at what actually drives those 5-star ratings (is it just the price, or something else?).
*   **For the Platform:** We analyze growth trends and the real impact of being a "Superhost."

## 📂 Project Structure
- `data/`: Raw and processed datasets (CSV).
- `notebooks/`: Sequential analysis steps from extraction to final prep.
- `docs/`: Data dictionary and technical documentation.
- `scripts/`: Production-ready ETL pipeline.
- `tableau/`: Visualization workbooks and dashboards.
- `reports/`: Project outlines and final reports.
- [`DVA-focused-Portfolio/`](DVA-focused-Portfolio/README.md): Team portfolio links (live sites & GitHub repos).
- [`DVA-oriented-Resume/`](DVA-oriented-Resume/README.md): Team resume links (Google Drive & Docs).

## 🚀 Analysis Workflow
1.  **Extraction:** Loading raw scrape data from Inside Airbnb.
2.  **Cleaning:** 3-pass cleaning process (dropping metadata, handling missing values, currency formatting).
3.  **EDA:** Multi-perspective visual exploration of pricing, demand, and quality.
4.  **Statistical Analysis:** Hypothesis testing (Superhost impact, Room type ANOVA) and Regression modeling.
5.  **Final Load & Prep:** Generating Tableau-optimized KPIs and summary aggregates.

## 🛠️ Installation & Setup
For detailed setup instructions, please refer to the following guides:

1.  **[How to Clone this Repository](docs/cloning_guide.md)**
2.  **[How to Setup Virtual Environment (.venv)](docs/setup_venv.md)**
3.  **[Business & Investment Insights (Market Analysis)](docs/BUSINESS_INSIGHTS.md)**

Quick Start:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 scripts/etl_pipeline.py
```

## 📊 Business KPIs (Ready for Tableau)
We have prepared a `tableau_ready.csv` that includes advanced business metrics:
*   **RevPAR:** Revenue Per Available Room (Standard industry benchmark).
*   **Investment Potential:** A weighted score (0-100) to identify top property opportunities.
*   **Market Segmentation:** Categorized price, revenue, and quality tiers.

### 🔗 Live Dashboards
Explore our interactive insights on Tableau Public:
*   **[All Live Dashboards & Screenshots](tableau/dashboard_links.md)**
*   **[Dashboard 1: Market Overview](https://public.tableau.com/app/profile/khushi.batra8374/viz/Book2_17774752683560/Dashboard1?publish=yes)**
*   **[Dashboard 2: Revenue & Pricing Strategy](https://public.tableau.com/app/profile/khushi.batra8374/viz/D2_DATA_17774765499930/D2_DashboardRevenuePricingStrategy?publish=yes)**
*   **[Dashboard 3: Investment Intelligence](https://public.tableau.com/app/profile/khushi.batra8374/viz/Book2_17774752683560/Dashboard3?publish=yes)**

## 👥 The Team — Section A, Group 5

| Contributor | Role | Profile | Resume | Portfolio |
| :--- | :--- | :--- | :--- | :--- |
| <img src="https://github.com/MAYANKSHARMA01010.png?size=80" width="80"><br>**Mayank Sharma** | **Project Lead** | [@MAYANKSHARMA01010](https://github.com/MAYANKSHARMA01010) | [📄 Resume](https://drive.google.com/drive/folders/1hyAqW57kYWOFdjWLKunGz9ghxRdwRbW_?usp=sharing) | [🌐 Portfolio](https://github.com/MAYANKSHARMA01010/DVA_PORTFOLIO) |
| <img src="https://github.com/MananGilhotra.png?size=80" width="80"><br>**Manan Gilhotra** | **Data Wizard** | [@MananGilhotra](https://github.com/MananGilhotra) | [📄 Resume](https://drive.google.com/file/d/15-ZkzoQhSKS6VJoKVXpTLRPJP7FCoPzw/view?usp=sharing) | [🌐 Portfolio](https://dva-prortfolio-eight.vercel.app/) |
| <img src="https://github.com/danieltayal07.png?size=80" width="80"><br>**Daniel Tayal** | **Research Guru** | [@danieltayal07](https://github.com/danieltayal07) | [📄 Resume](https://docs.google.com/document/d/17bhjIa4_JcdxQv4MC1QkrR3BNgHRHKdZyqFWiCVix2g/edit?usp=sharing) | [🌐 Portfolio](https://portfolio-danie.netlify.app) |
| <img src="https://github.com/vidhisinghal0101.png?size=80" width="80"><br>**Vidhi Singhal** | **Stats Master** | [@vidhisinghal0101](https://github.com/vidhisinghal0101) | — | — |
| <img src="https://github.com/abhiraj6386.png?size=80" width="80"><br>**Abhiraj Tripathi** | **Technical Architect** | [@abhiraj6386](https://github.com/abhiraj6386) | — | — |
| <img src="https://github.com/KHUSHI-612.png?size=80" width="80"><br>**Khushi Batra** | **Market Analyst** | [@KHUSHI-612](https://github.com/KHUSHI-612) | — | — |
| <img src="https://github.com/Mayank0875.png?size=80" width="80"><br>**Mayank Gupta** | **Documentation Lead** | [@Mayank0875](https://github.com/Mayank0875) | [📄 Resume](https://drive.google.com/file/d/16z82iqcc3aQewy2rVgxbtzI5AF0haK05/view?usp=sharing) | [🌐 Portfolio](https://dva-portfolio-jk67.onrender.com/) |

> 📁 Full details → **[Portfolio Links](DVA-focused-Portfolio/README.md)** · **[Resume Links](DVA-oriented-Resume/README.md)**

---
*Built with some late nights and a lot of coffee by Group 5 for our DVA Capstone 2 Project.*