import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('dark_background')

st.title("Corona statistics dashboard")


# Summed data as metrics
dfc = pd.read_csv("./data/corona_confirmed_ts_22-01-2022.csv", parse_dates=True)  # infection data
dfd = pd.read_csv("./data/corona_deaths_ts_22-01-2022.csv", parse_dates=True)  # deaths
t = dfc.columns.tolist()[4:]

dfc = dfc.groupby(by="Country/Region").sum()
dfd = dfd.groupby(by="Country/Region").sum()

denom = 3
conf = np.round(dfc.loc[:, t[-1]].sum() / 1e6, denom)
dconf = np.round((dfc.loc[:, t[-1]].sum() - dfc.loc[:, t[-2]].sum()) / 1e6, denom)

deaths = np.round(dfd.loc[:, t[-1]].sum() / 1e6, denom)
ddeaths = np.round((dfd.loc[:, t[-1]].sum() - dfd.loc[:, t[-2]].sum()) / 1e6, denom)

# Define columns
met1, met2, met3 = st.columns(3)

met1.metric(label="Confirmed Cases in millions", value=conf, delta=dconf)
met2.metric(label="Death Cases in millions", value=deaths, delta=ddeaths)
# add the vaccination numbers here as met3


# Later download the csv daily anew > link to github
df = pd.read_csv("./data/corona_confirmed_ts_22-01-2022.csv", parse_dates=True)

df = df.rename(columns={
    "Country/Region" : "country",
    "Province/State" : "state"})

ccountry = st.select_slider("Pick a country", options=df.country.tolist())
# have to remove the "states" here and sort alpabetically


ts_min = 4  # measurements begin
t = df.columns.tolist()[ts_min:]

dfg = df.groupby(by="country").sum() # can go upwards
dfg = dfg.reset_index()
idx = dfg[dfg.country == ccountry].index.tolist()
y = np.squeeze(dfg.loc[idx, t].values) / 1e6

# Def figure columns
col1, col2 = st.columns(2)

fig = plt.figure()
plt.plot(y)
plt.ylabel("Something")
col1.pyplot(fig)

fig = plt.figure()
plt.plot(np.diff(y))  # plot this in weeks
plt.ylabel("Something")
col2.pyplot(fig)
#st.line_chart(y)
