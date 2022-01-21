import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Later download the csv daily anew > link to github
df = pd.read_csv("./corona_ts.csv", parse_dates=True)

df = df.rename(columns={
    "Country/Region" : "country",
    "Province/State" : "state"})

st.title("Corona statistics dashboard")

ccountry = st.select_slider("Pick a country", options=df.country.tolist())
# have to remove the "states" here and sort alpabetically


ts_min = 4  # measurements begin
t = df.columns.tolist()[ts_min:]

dfg = df.groupby(by="country").sum() # can go upwards
dfg = dfg.reset_index()
idx = dfg[dfg.country == ccountry].index.tolist()
y = np.squeeze(dfg.loc[idx, t].values)

st.line_chart(y)
