import streamlit as st
import pandas as pd
import os

st.title("Data Quality Checker")
st.write("Upload your CSV or Excel file to analyze data quality")

uploaded_file = st.file_uploader("Choose a file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    # Read the file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
    
    # Display first 5 rows
    st.subheader("Data Preview")
    st.dataframe(df.head())
    
    # Dataset Overview Section
    st.subheader("Dataset Overview")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Rows", df.shape[0])
    with col2:
        st.metric("Total Columns", df.shape[1])
    with col3:
        file_size_mb = len(uploaded_file.getvalue()) / (1024*1024)
        st.metric("File Size", f"{file_size_mb:.2f} MB")
    
    # Column Details Section
    st.subheader("About the Columns")
    
    col_info = pd.DataFrame({
        'Data Type': df.dtypes,
        'Non-Null Count': df.count(),
        'Unique Values': df.nunique(),
        'Missing Values': df.isnull().sum(),
        'Missing %': round((df.isnull().sum() / len(df)) * 100, 2)
    })
    
    st.dataframe(col_info, use_container_width=True)
    
    # Data Quality Issues Section
    st.subheader("Data Quality Issues")
    
    col1, col2 = st.columns(2)
    
    with col1:
        duplicate_count = df.duplicated().sum()
        st.metric("Duplicate Rows", duplicate_count)
    
    with col2:
        total_missing = df.isnull().sum().sum()
        st.metric("Total Missing Values", total_missing)
    
    # Columns with issues
    st.write("**Columns with Missing Data:**")
    missing_cols = df.isnull().sum()[df.isnull().sum() > 0]
    if len(missing_cols) > 0:
        st.dataframe(missing_cols.reset_index().rename(columns={'index': 'Column', 0: 'Missing Count'}))
    else:
        st.success("No missing values found!")

else:
    st.info("Please upload a CSV or Excel file to get started")