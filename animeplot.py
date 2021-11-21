import pandas as pd
# import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import os
import plotly.express as px
import logging
###### begin logger config
logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('/tmp/animeplot.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -\n %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)
# WHO API LINK
# https://extranet.who.int/xmart-api/odata/NCOV_PHM/CLEAN_PHSM
st.title("001 data_anime Data")
DATA_URL =  "dataset/data_anime.csv"
@st.cache
def load_data():
	data = pd.read_csv(DATA_URL)
	logger.debug(data.head())
	return data


data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text("Done! (using st.cache)")

show_data_bol = st.sidebar.checkbox("Show Raw data")
if show_data_bol:
	st.subheader('Raw data')
	st.write(data)


# logger.debug(data.loc[(data.rating>9.0) & (data.type == "TV")])
st.subheader('Top 10 best rating > 9.0 anime by TV')
data_ratingtv = (data.loc[(data.rating>9.0) & (data.type == "TV")])
data_ratingtv = data_ratingtv.sort_values(by='rating', ascending = False)
st.table(data_ratingtv)
columns = ["rating"]
for x in columns:	
	fig = px.treemap(data.loc[(data.rating>9.0) & (data.type == "TV")],path=['name','genre'],values=x,title="treemap Anime  %s" %x)
	st.plotly_chart(fig)

st.subheader('Top 10 best rating >8.0 anime by MOVIE')
data_ratingmovie = (data.loc[(data.rating>8.0) & (data.type == "Movie")])
data_ratingmovie = data_ratingmovie.sort_values(by='rating', ascending = False)
st.table(data_ratingmovie[:10])
columns = ["rating"]
for x in columns:	
	fig = px.treemap(data_ratingmovie[:10],path=['name','genre'],values=x,title="treemap Anime  %s" %x)
	st.plotly_chart(fig)

st.subheader('Top 10 best rating >8.0 anime by OVA ')

data_ratingova = (data.loc[(data.rating>8.0) & (data.type == "OVA")])
data_ratingova = data_ratingova.sort_values(by='rating', ascending = False)
st.table(data_ratingova[:10])
columns = ["rating"]
for x in columns:	
	fig = px.treemap(data_ratingova[:10],path=['name','genre'],values=x,title="treemap Anime  %s" %x)
	st.plotly_chart(fig)