import streamlit as st
import pandas as pd
import pickle


with open('model.pkl', 'rb') as f:
    reg = pickle.load(f)


st.title('Car Price Predictor')
st.text('Mention : Car company, Car model, Year, Kms_driven, Fuel_type')


df = pd.read_csv('cleaned_car.csv')

unique_brand = df['company'].unique()

company = st.selectbox("Company",unique_brand)
model_data = df[df['company']==company]['name'].unique()
model = st.selectbox("Model",model_data)
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
