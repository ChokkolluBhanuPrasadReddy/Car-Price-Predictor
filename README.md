Car Price Production
This is a simple web app that predicts car prices using a trained machine learning model. The app is built and deployed using Streamlit.

Overview
The project takes car details like year, mileage, fuel type, and transmission, and predicts the selling price using a regression model.

You can check the demo here: [Car Price Prediction App](https://car-price-predictor-cvjhrhbtpcgefejiauwaen.streamlit.app/)


Features
Predicts car prices based on input features
Simple and interactive Streamlit interface
Easy to run locally or deploy online

Technologies Used
Python
pandas, numpy
scikit-learn
Streamlit
pickle (for loading model)

Project Structure
app.py
model.pkl
requirements.txt
README.md

How to Run
Clone this repository.
Open the folder in your terminal.
Install required libraries:
pip install -r requirements.txt

Run the app:
streamlit run app.py

The app will open in your browser.
Deployment

This project is deployed using Streamlit Cloud.
You can deploy by connecting your GitHub repository to Streamlit Cloud and selecting app.py as the main file.

Files
app.py: Main Streamlit app
model.pkl: Trained machine learning model
requirements.txt: List of dependencies

Example
Enter details like car name, year, fuel type, kilometers driven, etc., and the app will show the predicted price.
