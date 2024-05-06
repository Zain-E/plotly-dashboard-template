import pandas as pd
import streamlit as st
import datetime

df = pd.read_csv('/Users/zaineisa/Documents/VSCode/historic_weather/df.csv',parse_dates=['date'])
#df['date'] = pd.to_datetime(df['date'], errors='coerce')
# column_types = df.dtypes
# print(column_types)

print(df)
country_list = [col for col in df['country'].unique() if col != 'country']

# min_date = df['date'].min()
# max_date = df['date'].max()
# selected_date = st.slider('Select a date', min_value=min_date, max_value=max_date,value=datetime.datetime(2023, 4, 1))
# filtered_df = df[df['date'] == selected_date]

st.title("Historic Weather Dashboard")
selected_country = st.radio('Select a country', country_list)
filtered_df = df[df['country'] == selected_country]
line_chart_data = filtered_df[['date','temperature_2m_mean','country']]

st.subheader(f'{selected_country}')
st.line_chart(data=filtered_df, x='date', y='temperature_2m_mean', color='country', use_container_width=True)
#st.write(line_chart_data)


