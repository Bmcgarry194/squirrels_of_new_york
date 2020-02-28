import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.title('King County House Sales in 2014')

@st.cache
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/bmcgarry194/knn_workshop/master/data/kc-house-data.zip")

    renamed = df.rename(columns={'long': 'lon'})
    renamed['month_sold'] = pd.to_datetime(renamed['date']).dt.month
    return renamed

renamed = load_data()
# default_zips = [98144, 98112, 98122, 98134, 98109, 98119]

multi = st.multiselect("Zipcodes", list(renamed['zipcode'].unique()), default=list(renamed['zipcode'].unique()))

min_price = renamed['price'].min()
max_price = renamed['price'].max()
low, high = st.sidebar.slider('Price Range', min_value=int(min_price), max_value=int(max_price), value=(int(min_price), int(max_price)))

month_data = renamed.loc[(renamed['price'] >= low) &
                         (renamed['price'] <= high) &
                         (renamed['zipcode'].isin(multi)), :]

st.deck_gl_chart(viewport={'latitude': 47.6062,
                           'longitude': -122.3321,
                           'zoom': 10,},
                layers=[{'type': 'ScatterplotLayer',
                         'data': month_data,
                         'opacity': .5,
                         'radiusScale': .9}])

st.sidebar.subheader('Histogram of House Prices')
hist_values = np.histogram(month_data['price'], bins=24)[0]
st.sidebar.bar_chart(hist_values)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(month_data)
    
btn = st.button("Celebrate!")
if btn:
    st.balloons()