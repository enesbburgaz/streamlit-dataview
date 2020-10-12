from datetime import date
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.title('Google Play Store Apps')

name = st.text_input('Name')
if not name:
    st.stop()
st.write('Hi', name)
st.success('Thank you for inputting a name.')

data = pd.read_csv('googleplaystore.csv')
if st.checkbox('Show Dataset'):
    st.write(data)

st.write('Total app counts, ',data['App'].count())

st.write('Category Counts')
st.bar_chart(data['Category'].value_counts())

st.write('Top 20 App')
st.write(data.sort_values('Installs', ascending=False)[:20])

st.sidebar.write('Personal Information')
st.sidebar.write(f'Hi {name}')
age = st.sidebar.slider(f'{name} How old are you?', 0, 130, 25)
st.sidebar.write("I'm ", age, 'years old')

add_selectbox = st.sidebar.selectbox(
    "Job Type",
    ("Student","Test")
)

city = st.sidebar.text_input('City')
email = st.sidebar.text_input('Email')
