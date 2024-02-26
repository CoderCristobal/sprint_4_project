import streamlit as st
import pandas as pd
import plotly_express as px

df = pd.read_csv('vehicles_us.csv')
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

st.header('Data viewer')

filter_price = st.checkbox('Filter by Price')
if filter_price:
    start_price, end_price = st.select_slider(
        'Select Price Range',
        options=df['price'].sort_values().unique(),
        value=(1, 10000))
    df = df[(df['price'] >= start_price) & (df['price'] <= end_price)].sort_values(by='price')

filter_model_year = st.checkbox('Filter by Model Year')
if filter_model_year:
    df = df.dropna(subset='model_year')
    start_year, end_year = st.select_slider(
        'Select Year Range',
        options=df['model_year'].sort_values().unique(),
        value=(1908, 2019))
    df = df[(df['model_year'] >= start_year) & (df['model_year'] <= end_year)].sort_values(by='model_year')

filter_condition = st.checkbox('Filter by Condition')
if filter_condition:
    selected_conditon = st.selectbox(
        'Select Condition',
        options=df['condition'].unique()
    )
    df = df[df['condition'] == selected_conditon]

filter_cylinders = st.checkbox('Filter by Cylinders')
df = df.dropna(subset='cylinders')
if filter_cylinders:
    start_cylinder, end_cylinder = st.select_slider(
        'Select Cylinder Range',
        options=df['cylinders'].sort_values().unique(),
        value=(3, 4)
    )
    df = df[(df['cylinders'] >= start_cylinder) & (df['cylinders'] <= end_cylinder)]

filter_fuel = st.checkbox('Filter by Fuel')
if filter_fuel:
    selected_fuel = st.selectbox(
        'Select Fuel Type',
        options=df['fuel'].unique())
    df = df[df['fuel'] == selected_fuel]

filter_odometer = st.checkbox('Filter by Odometer')
if filter_odometer:
    df = df.dropna(subset='odometer')
    start_miles, end_miles = st.select_slider(
        'Select Mile Range',
        options=df['odometer'].sort_values().unique(),
        value=(47000, 108000))
    df = df[(df['odometer'] >= start_miles) & (df['odometer'] <= end_miles)]

filter_transmition = st.checkbox('Filter by Transmission')
if filter_transmition:
    selected_transmition = st.selectbox(
        'Select Transmission Type',
        options=df['transmission'].unique()
    )
    df = df[df['transmission'] == selected_transmition]

filter_color = st.checkbox('Filter by Color')
if filter_color:
    df = df.dropna(subset='paint_color')
    selected_color = st.selectbox(
        'Select a Color',
        options=df['paint_color'].unique()
    )
    df = df[df['paint_color'] == selected_color]

filter_4wd = st.checkbox('Filter by 4 Wheel Drive')
if filter_4wd:
    df['is_4wd'] = df['is_4wd'].fillna(0)
    toggle_4wd = st.checkbox('Has 4 Wheel Drive')
    if toggle_4wd:
        df = df[df['is_4wd'] == 1]
    else:
        df = df[df['is_4wd'] == 0]
    
filter_manufacturer = st.checkbox('Filter by Manufacturer')
if filter_manufacturer:
    maker = st.selectbox(
        'Select Manufacturer',
        options=df['manufacturer'].unique())
    df = df[df['manufacturer'] == maker]


st.dataframe(df)