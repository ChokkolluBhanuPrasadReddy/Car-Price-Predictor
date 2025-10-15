import streamlit as st
import joblib
import pandas as pd



reg = joblib.load('model.pkl')
st.title('Car Price Predictor')
st.text('Mention : Car company, Car model, Year, Kms_driven, Fuel_type')


df = pd.read_csv('cleaned_car.csv')

unique_model = df['name'].unique()
unique_brand = df['company'].unique()

company = st.selectbox("Company",unique_brand)
model = st.selectbox("Model",unique_model)
year = st.number_input("Year",2001,2025,2015)
kms = st.number_input("KMs Driven",10,None,10000)
fuel_type = st.selectbox("Fuel Type",['Petrol','Diesel'])

data = pd.DataFrame([[model,company,year,kms,fuel_type]],columns=['name','company','year','kms_driven','fuel_type'])
predicted = reg.predict(data)

predicted_float = float(predicted[0])
formatted = f"₹{predicted_float:,.2f}"

if st.button('Evaluate') :
    if not company or not model:
        st.warning("Enter valid Car Company Name or Car model")
    else :
        st.write(formatted)
