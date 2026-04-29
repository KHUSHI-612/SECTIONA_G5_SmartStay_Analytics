# 🐍 Setting Up Your Python Environment

To run our analysis scripts and notebooks, you'll need to set up a Virtual Environment. This keeps our project dependencies separate from your other work and prevents "it works on my machine" issues.

### 1. Create the Environment
In your terminal, within the project folder, run:
```bash
python3 -m venv .venv
```
*This creates a folder named `.venv` that will hold all our Python tools.*

### 2. Activate It
You need to tell your computer to use this specific environment:
*   **macOS / Linux:**
    ```bash
    source .venv/bin/activate
    ```
*   **Windows:**
    ```powershell
    .\venv\Scripts\activate
    ```

### 3. Install Dependencies
Now, install the libraries we used (like Pandas, Matplotlib, and Scikit-learn):
```bash
pip install -r requirements.txt
```

### 4. You're Ready!
You can now run the ETL pipeline:
```bash
python3 scripts/etl_pipeline.py
```

*Note: If you are using VS Code, make sure to select the `.venv` kernel when opening our Jupyter Notebooks.*
