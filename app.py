import streamlit as st
import numpy as np


st.title('AlternusVera Dashboard')

process_function = st.selectbox('Choose an Action', ['None', 'Process New News'])

if process_function == 'Process New News':
    st.header('Collecting News from Sources')
    st.subheader('Description')
    st.write('Test Write')
    st.markdown(r'Test Write')
    st.write('Test Write')

