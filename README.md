A corona stats dashboard using streamlit.

The notebook [explore-data.ipynb]() visualizes various corona statistics.
The interesting results from this exploration are then integrated into the streamlit app. 

```
pip3 install millify
```

```
streamlit run app.py
```

Reading the .CSV files from URL requires the "RAW" data link eg: `https://raw.githubusercontent.com/...`

### Streamlit info
deploy app: https://share.streamlit.io/signup (Once deployed, reachable: https://share.streamlit.io/mikehemberger/corona-dashboard/main/app.py
)
python api: https://docs.streamlit.io/library/api-reference

### Data and sources
- Infection numbers timeseries: https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv
- Virus variants: https://www.ecdc.europa.eu/en/publications-data/data-virus-variants-covid-19-eueea
- Big diverse data: https://www.ecdc.europa.eu/en/covid-19/data
- RKI dashboard: https://experience.arcgis.com/experience/478220a4c454480e823b17327b2bf1d4/page/Bundesl%C3%A4nder/

Omicron timeline - https://cdn.knightlab.com/libs/timeline3/latest/embed/index.html?source=1XjAYFLM5Rvh9l9ySqMbb_NVkWRpKsSQBDmwytmPdLUg&font=Default&lang=en&initial_zoom=2&height=650

B.1.1.529 - Omicron