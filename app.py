import streamlit as st
from news_articles import extract_rss_feeds
import numpy as np
import json

st.title('AlternusVera Dashboard')

cdn_repo = "https://raw.githubusercontent.com/aryan-jadon/machine-learning-dashboard/master/cdn_model_weights/{" \
           "file_name}.pkl "
cdn_json = "https://raw.githubusercontent.com/aryan-jadon/machine-learning-dashboard/master/rss/news_sources.json"

process_function = st.selectbox('Choose an Action', ['None', 'Process New News'])

if process_function == 'Process New News':
    st.header('Collecting News from Sources')
    st.write('Loading Model Weights')
    with open(cdn_json, 'r') as f:
        news_sources = json.load(f)

    st.write(news_sources)
    # st.dataframe(df)

    st.subheader('Description')
    st.write('Loading Model Weights')
    naive_bayes_weights = cdn_repo.format(file_name="NaiveBayes")
    st.write('Loading Naive Bayes Weights')
    SVM_weights = cdn_repo.format(file_name="SVM")
    st.write('Loading SVM Weights')
