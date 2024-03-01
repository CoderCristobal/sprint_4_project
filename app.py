import streamlit as st
import pandas as pd
import plotly_express as px

#Loading DF
df = pd.read_csv('vehicles_us.csv')

#Changing 'date_posted' to datetime data type
df['date_posted'] = pd.to_datetime(df['date_posted'])

#Filling missing values in 'is_4wd' with 0 and changing to int data type
df['is_4wd'] = df['is_4wd'].fillna(0).astype('int64')

#Cleaning model column
df['model'] = df['model'].str.replace('f150', 'f-150')
df['model'] = df['model'].str.replace('f250', 'f-250')
df['model'] = df['model'].str.replace('f350', 'f-350')
df['model'] = df['model'].str.replace('sd', 'super duty')

#Adding Manufacturer column from the frist word in Model string
df['manufacturer'] = df['model'].apply(lambda x: x.split()[0])

#Removing Manufacturer from Model
df['model'] = df['model'].apply(lambda x: ' '.join(x.split()[1:]))

#Presenting DF
st.title('Car Listing Viewer')
st.dataframe(df)

st.header('A graph of availability by odometer/price')

#Checkbox for altering histogram
is_price = st.checkbox('Availability by Price')
if is_price:
    x_hist_value = 'price'
else:
    x_hist_value = 'odometer'

#Histogram
st.write(px.histogram(df, x=x_hist_value, color='condition'))

st.header('Price checker by model and year')
#Getting filter for scatterplot
selected_model = st.selectbox(
        'Select Model Type',
        options=df['model'].unique()
)

selected_condition = st.selectbox(
    'Select Condition',
    options=df['condition'].unique()
)

filtered_models = df.loc[(df['model'] == selected_model) & (df['condition'] == selected_condition)]

#Scatterplot

st.write(px.scatter(filtered_models, x='model_year', y='price', title=f'Prices of {selected_model} in {selected_condition} condition'))

#Making df for average price by model and year
target_model = df.dropna()
target_model = target_model[target_model['model'] == selected_model][target_model['condition'] == selected_condition]
target_model = target_model.dropna(subset=['model_year'])
target_model['model_year'] = target_model['model_year'].astype('int64')

#Getting average
avg_model_price = target_model.groupby('model_year')['price'].mean().reset_index(name='avg_price')

#DF and Bargraph
st.write(px.bar(avg_model_price, x='model_year', y='avg_price', title=f'Average price of {selected_model} in {selected_condition} condition by year'))
st.write(avg_model_price)