import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('india_economy.csv')

# Create a function to plot the time series data
def plot_time_series(df, column):
  fig, ax = plt.subplots()
  ax.plot(df[column])
  ax.set_xlabel('Time')
  ax.set_ylabel(column)
  ax.set_title('Time Series of ' + column)
  return fig

# Create a function to perform a simple linear regression on the time series data
def simple_linear_regression(df, column1, column2, parameter):
  x = df[column1]
  y = df[column2]
  slope, intercept = np.linalg.lstsq(x.values.reshape(-1, 1), y.values, rcond=-1)[0]
  if parameter == 'slope':
      return slope
  elif parameter == 'intercept':
      return intercept
  else:
      raise ValueError('Parameter should be "slope" or "intercept"')

# Create a function to plot the time series data with a linear regression line
def plot_time_series_with_regression_line(df, column1, column2):
  fig, ax = plt.subplots()
  ax.plot(df[column1])
  slope, intercept = simple_linear_regression(df, column1, column2)
  ax.plot(df[column1], slope * df[column1] + intercept)
  ax.set_xlabel('Time')
  ax.set_ylabel(column2)
  ax.set_title('Time Series of ' + column2 + ' with Linear Regression Line')
  return fig

# Create a sidebar with options for the user to select the data to plot and the type of analysis to perform
st.sidebar.markdown('**Select the data to plot:**')
column_options = ['GDP', 'Industrial production', 'Retail sales', 'Unemployment rate', 'Inflation rate', 'Interest rates', 'Exchange rates']
column = st.sidebar.selectbox('Column', column_options)

# Create a main section with the plot
st.markdown('**Plot of the time series data:**')
fig = plot_time_series(df, column)
st.pyplot(fig)

# If the user selects to perform a linear regression, create a section with the regression line
if st.sidebar.checkbox('Perform a linear regression?'):
  st.markdown('**Linear regression line:**')
  fig = plot_time_series_with_regression_line(df, column, column)
  st.pyplot(fig)
