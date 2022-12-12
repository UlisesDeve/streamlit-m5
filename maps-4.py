import streamlit as st
import pandas as pd

#DATA_URL = 'uber-raw-data-sep14.csv'    #Original
DATA_URL = 'https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz' 
DATE_COLUMN = 'Date/Time'

@st.cache
def load_data(number_rows):
  data = pd.read_csv(DATA_URL, nrows = number_rows)
  lowercase = lambda x: str(x).lower()
  data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
  data.rename(lowercase, axis='columns', inplace=True)
  return data

data = load_data(1000) 
st.dataframe(data)

st.map(data)