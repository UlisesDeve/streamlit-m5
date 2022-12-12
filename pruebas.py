import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#--- IMPORT DATA ---#
df=pd.read_csv("kpis.csv")

gender = st.sidebar.multiselect("Select Gender",
                                options=df['gender'].unique(),
                                default=df['gender'].unique())

st.sidebar.markdown("##")
performance_score= st.sidebar.multiselect("Select the Performance Score",
                                          options=df['performance_score'].unique(),
                                          default=df['performance_score'].unique())
st.sidebar.markdown("##")
marital_status= st.sidebar.multiselect("Select Marital Status",
                                       options=df['marital_status'].unique(),
                                       default=df['marital_status'].unique())

df_selection=df.query("gender == @gender & performance_score == @performance_score & marital_status == @marital_status")

st.write(df_selection)

avg_hours_gender=(
    df_selection.groupby(by=['gender']).sum()
[['average_work_hours']].sort_values(by="average_work_hours"))

st.write(avg_hours_gender)


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])
st.write(chart_data)