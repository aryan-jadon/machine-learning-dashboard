import streamlit as st
import numpy as np


st.title('AlternusVera Dashboard')

cdn_repo = "https://raw.githubusercontent.com/aryan-jadon/machine-learning-dashboard/master/cdn_model_weights/{file_name}.pkl"

process_function = st.selectbox('Choose an Action', ['None', 'Process New News'])

if process_function == 'Process New News':
    st.header('Collecting News from Sources')
    st.subheader('Description')
    st.write('Loading Model Weights')
    naive_bayes_weights = cdn_repo.format(file_name="NaiveBayes")
    st.write('Loading Naive Bayes Weights')
    SVM_weights = cdn_repo.format(file_name="SVM")
    st.write('Loading SVM Weights')

