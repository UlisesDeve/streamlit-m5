import pandas as pd
import streamlit as st

names_link = 'dataset_2.csv'
names_data = pd.read_csv(names_link)
st.title('Streamlit con pandas')
st.dataframe(names_data)