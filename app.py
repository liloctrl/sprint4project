# Import necessary libraries
import streamlit as st
import plotly.express as px
import pandas as pd


#Load data

df = pd.read_csv('vehicles_us.csv')

# Sample data (replace this with loading your actual dataset)
data = {
    'price': [14990, 15990, 19500, 12990, 14990, 13990, 12500, 7500, 5000, 3890, 8000, 11499, 5100, 11200, 10400, 30300, 13000, 16999, 14950, 1900, 23800, 16500, 11950, 4826, 18000],
    'odometer': [57954, 109473, 128413, 132285, 130725, 100669, 128325, 180000, 137273, 300000, 234000, 54772, 188000, 90302, 111871, 30339, 146000, 137230, 114773, 207, 10899, 123262, 170000, 226111, 50500],
    'model_year': [2014, 2013, 2011, 2009, 2010, 2014, 2013, 2004, 2009, 2011, 2009, 2017, 2008, 2015, 2012, 2017, 2005, 2013, 2012, 1994, 2019, 2012, 2008, 2000, 2010]
}

# Streamlit header
st.header("Vehicle Data Analysis")

# Histogram of Price
st.subheader("Price Distribution of Vehicles")

fig_price = px.histogram(df, x='price', nbins=20, title='Distribution of Vehicle Prices')

st.plotly_chart(fig_price)

# Scatter Plot of Price vs. Odometer

st.subheader("Price vs. Odometer Scatter Plot")

fig_price_odometer = px.scatter(df, x='odometer', y='price', title='Price vs. Odometer', labels={'odometer': 'Odometer (miles)', 'price': 'Price ($)'})
st.plotly_chart(fig_price_odometer)

# Checkbox to display another scatter plot for Odometer vs. Model Year

if st.checkbox("Show Odometer vs. Model Year Scatter Plot"):

    fig_odometer_model_year = px.scatter(df, x='model_year', y='odometer', title='Odometer vs. Model Year',labels={'model_year': 'Model Year', 'odometer': 'Odometer (miles)'})
    st.plotly_chart(fig_odometer_model_year)
