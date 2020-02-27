import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('Squirrels of New York')

df = pd.read_csv('data/squirrel_census.csv')

renamed = df.rename(columns={'X': 'lon', 'Y': 'lat'})
renamed['date_time'] = pd.to_datetime(renamed['Date'], format='%m%d%Y')
renamed['day'] = renamed['date_time'].dt.day

days = renamed['date_time'].dt.day
day = st.slider('Date Range', min_value=6, max_value=20)

day_data = renamed.loc[renamed['day'] == day, :]

st.deck_gl_chart(viewport={'latitude': 40.7829,
                           'longitude': -73.9654,
                           'zoom': 13,},
                layers=[{'type': 'ScatterplotLayer',
                         'data': day_data,
                         'opacity': .5,
                         'radiusScale': .3}])

st.bar_chart(day_data['Primary Fur Color'])