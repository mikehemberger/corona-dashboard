import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from millify import millify

plt.rc('font', size=15)
plt.style.use('dark_background')

# Summed data as metrics
url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv"
dfc = pd.read_csv(url, parse_dates=True)  # infection data

url = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv"
dfd = pd.read_csv(url, parse_dates=True)

t = dfc.columns.tolist()[4:]

dfc = dfc.groupby(by="Country/Region").sum()
dfd = dfd.groupby(by="Country/Region").sum()

conf = dfc.loc[:, t[-1]].sum()
dconf = dfc.loc[:, t[-1]].sum() - dfc.loc[:, t[-2]].sum()

deaths = dfd.loc[:, t[-1]].sum()
ddeaths = dfd.loc[:, t[-1]].sum() - dfd.loc[:, t[-2]].sum()

# Streamlit start
st.title("Corona statistics dashboard " + t[-1])

# Define columns
met1, met2, met3 = st.columns(3)

met1.metric(label="Confirmed Cases", value=millify(conf, precision=2), delta=millify(dconf, precision=2))
met2.metric(label="Death Cases", value=millify(deaths, precision=2), delta=millify(ddeaths, precision=2))
# add the vaccination numbers here as met3

# Later download the csv daily anew > link to github
df = pd.read_csv("./data/corona_confirmed_ts_22-01-2022.csv", parse_dates=True)

df = df.rename(columns={
    "Country/Region" : "country",
    "Province/State" : "state"})

ts_min = 4  # measurements begin
t = df.columns.tolist()[ts_min:]
#tt = len(df.columns.tolist()) - ts_min

dfg = df.groupby(by="country").sum() # can go upwards
dfg = dfg.reset_index()

ccountry = st.sidebar.select_slider("Select a country", options=dfg.country.tolist())
# have to remove the "states" here and sort alpabetically
idx = dfg[dfg.country == ccountry].index.tolist()

# Accumulated infections
y = np.squeeze(dfg.loc[idx, t].values) / 1e6

# Rolling average over daily new infected
prev = st.sidebar.select_slider("Show last days", options=range(len(t)))
t_prev = t[-prev:]

#y2 = np.squeeze(dfg.loc[idx, t].diff(axis=1).transpose().rolling(window=7).mean())
y2 = np.squeeze(dfg.loc[idx, t_prev].diff(axis=1).transpose().rolling(window=7).mean())
y2 = np.array(y2)
#y2 = dfg.loc[idx, t].diff(axis=1).T.rolling(window=7).mean()

# Def figure columns
col1, col2 = st.columns(2)

fig = plt.figure(figsize=(4,4))
plt.plot(y)
plt.ylabel("Accumulated infections (Mio.)")
col1.pyplot(fig)

fig = plt.figure(figsize=(4,4))
plt.plot(y2)  # plot this in weeks
plt.ylabel("Daily infections")
col2.pyplot(fig)
#st.line_chart(y)
