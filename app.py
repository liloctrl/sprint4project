# Import necessary libraries
import streamlit as st
import plotly.express as px
import pandas as pd


#Load data

df = pd.read_csv('vehicles_us.csv')

# Sample data (replace this with loading your actual dataset)

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
