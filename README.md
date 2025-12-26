# Data Quality Checker

A Streamlit web application for analyzing data quality in CSV and Excel files.

## Live Demo

[https://data-quality-checker02.streamlit.app/](https://data-quality-checker02.streamlit.app/)

## Features

- Upload CSV or Excel files
- Data preview (first 5 rows)
- Dataset overview (rows, columns, file size)
- Column-wise analysis (data types, null counts, unique values)
- Missing data detection and visualization
- Duplicate row identification
- Missing value percentage calculation

## Technologies Used

- Python
- Streamlit
- Pandas

## Installation
```bash
pip install streamlit pandas
```

## Usage

Run locally:
```bash
streamlit run app.py
```

Upload your CSV or Excel file and get instant data quality insights.

## What It Analyzes

1. **Dataset Metrics**: Total rows, columns, and file size
2. **Column Details**: Data types, non-null counts, unique values
3. **Missing Data**: Count and percentage of missing values per column
4. **Duplicates**: Identifies and displays duplicate rows
5. **Data Quality Issues**: Summary of all data quality problems

## Output

- Interactive data preview table
- Comprehensive column information table
- Highlighted data quality issues
- List of columns with missing data
- Duplicate rows display
