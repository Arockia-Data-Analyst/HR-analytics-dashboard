import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="HR Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)

st.sidebar.title("HR Analytics")

st.sidebar.info("""
This project analyzes employee attrition using Microsoft Power BI.

Created by:
Arockia Jebarani M
""")

# Title
st.title("📊 HR Analytics Dashboard")
st.subheader("Employee Attrition Analysis")

st.markdown("---")

# Project Description
st.header("Project Overview")

st.write("""
This HR Analytics Dashboard was developed using **Microsoft Power BI** to analyze
employee attrition and workforce trends.

The dashboard helps HR professionals identify:
- Employee Attrition
- Salary Distribution
- Department Performance
- Employee Age Distribution
- Gender-wise Analysis
""")

st.markdown("---")

# Dashboard Image
st.header("Dashboard")

image = Image.open("dashboard.png")
st.image(image, use_container_width=True)

st.markdown("---")

# KPI Section
st.header("Key Performance Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Employees", "1470")
col2.metric("Employees Left", "237")
col3.metric("Average Monthly Income", "6.50K")
col4.metric("Average Employee Age", "36.92")

st.markdown("---")

# Insights
st.header("Key Insights")

st.success("Research & Development department has the highest employee attrition.")

st.info("Most employees belong to the 30–40 years age group.")

st.warning("Managers and Research Directors receive the highest salaries.")

import pandas as pd

st.markdown("---")
st.header("Employee Dataset")

df = pd.read_csv("HR Analytics Dataset.csv")

st.dataframe(df)
st.download_button(
    label="📥 Download HR Dataset",
    data=open("HR Analytics Dataset.csv", "rb"),
    file_name="HR_Analytics_Dataset.csv",
    mime="text/csv"
)
