Here’s a clean README file specifically for the main.py you uploaded:

---

# 📊 Startup Funding Analysis

## 📌 Overview

This project analyzes *Indian startup funding data* from startup_funding.csv.
It cleans the data, extracts insights, and visualizes trends related to *years, sectors, cities, startups, investors, and investment types*.

---

## 📂 Files

* **main.py** → Python script that performs:

  * Data cleaning & preprocessing
  * Aggregations & summaries
  * Visualizations
* **startup_funding.csv** → Dataset containing startup funding details (must be placed in the correct path)

---

## 🛠 Requirements

Install the required Python libraries:

bash
pip install pandas matplotlib seaborn


---

## ▶ How to Run

1. Place startup_funding.csv in the project directory or update the path in main.py:

   python
   df = pd.read_csv('startup_funding.csv')
   
2. Run the script:

   bash
   python main.py
   
3. The script will:

   * Display cleaned dataset previews
   * Print funding summaries
   * Show charts for trends and rankings

---

## 🔍 Script Workflow

### 1. *Data Cleaning*

* Fill missing values in categorical columns with "Unknown".
* Remove , and + from *Amount in USD* and convert to numeric.
* Convert date column to datetime format.
* Standardize text (lowercase, trimmed spaces).

### 2. *Feature Engineering*

* Extract *FundingYear* and *FundingMonth*.

### 3. *Data Aggregation*

* Yearly & monthly funding trends
* Top sectors by funding
* Top cities by funding
* Top startups by funding
* Top investors (by funding & number of deals)
* Funding by investment type

### 4. *Visualizations*

* *Line plots* for yearly funding trends.
* *Bar charts* for:

  * Top sectors
  * Top cities
  * Top startups
  * Top investors
  * Investment types

---

## 📊 Output Examples

* *Yearly Trends*
* *Top 10 Sectors*
* *Top 10 Cities*
* *Top 10 Startups*
* *Top 10 Investors*
* *Top Investment Types*

---

## ⚠ Notes

* Fix City.head(10) to city_funding.head(10) to avoid errors.
* The column InvestmentnType may be a typo — confirm it matches the dataset.
* Adjust dataset path if not using /content/startup_funding.csv.

---

