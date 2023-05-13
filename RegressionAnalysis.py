import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Load the data
df = pd.read_csv("covid_data.csv")

# Define a function to calculate the odds ratio
def odds_ratio(df, condition):
    a = df[(df["Underlying health condition"] == condition) & (df["COVID-19"] == "Yes")].shape[0]
    b = df[(df["Underlying health condition"] != condition) & (df["COVID-19"] == "No")].shape[0]
    c = df[(df["Underlying health condition"] != condition) & (df["COVID-19"] == "Yes")].shape[0]
    d = df[(df["Underlying health condition"] == condition) & (df["COVID-19"] == "No")].shape[0]
    odds_ratio = (a*d) / (b*c)
    return odds_ratio

# Define a function to create a plot
def create_plot(df):
    fig = px.bar(df, x="Underlying health condition", y="Odds ratio", title="Odds ratio for underlying health condition due to Covid - 19 (Regression Analysis)")
    st.plotly_chart(fig)

# Define the Streamlit app
def app():
    st.title("COVID-19 and Underlying Health Conditions")

    # Sidebar
    st.sidebar.title("Select an underlying health condition")
    condition = st.sidebar.selectbox("", df["Underlying health condition"].unique())

    # Calculate odds ratio and display results
    if condition:
        ratio = odds_ratio(df, condition)
        st.write(f"Odds ratio for {condition}: {ratio:.2f}")
        st.write("People with", condition, "are", f"{ratio:.2f}", "times more likely to get COVID-19 than those without.")
    else:
        st.warning("Please select an underlying health condition from the sidebar.")

    # Display plot
    create_plot(df)

    st.write(df)

app()