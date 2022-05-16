import pandas as pd
import streamlit as st
import numpy as np
import json

st.title('AlternusVera Dashboard')

cdn_repo = "https://raw.githubusercontent.com/aryan-jadon/machine-learning-dashboard/master/cdn_model_weights/{" \
           "file_name}.pkl "
cdn_json = "https://raw.githubusercontent.com/aryan-jadon/machine-learning-dashboard/master/rss/news_sources.json"

process_function = st.selectbox('Choose an Action', ['None',
                                                     'Run Analysis'])

if process_function == 'Run Analysis':
    st.header('Collecting News from Sources')
    news_file = pd.read_excel("https://machine-learning-articles.s3.us-west-2.amazonaws.com/05-16-2022.xlsx")
    st.dataframe(news_file)