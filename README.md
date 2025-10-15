Car Price Predictor
A machine learning web application that predicts used car prices based on features like brand, year, mileage, fuel type, and transmission. Built with Python and deployed using Streamlit for interactive use.

Features
- Predicts car prices using regression models
- Interactive form for user input
- Real-time output with confidence score
- Simple and responsive user interface
Tech Stack
- Python (Pandas, NumPy, Scikit-learn)
- Streamlit for deployment
- Pickle for model serialization
- Optional: Matplotlib/Seaborn for visualizations

How to Run Locally
- Clone the repository
git clone https://github.com/your-ChokkolluBhanuPrasadReddy/car-price-predictor.git
- Install dependencies
pip install -r requirements.txt
- Launch the app
streamlit run app.py

Folder Structure
car-price-predictor/
│
├── app.py               # Streamlit app
├── model.pkl            # Trained regression model
├── data/                # Raw and cleaned datasets
├── utils.py             # Helper functions
├── README.md            # Project overview
└── requirements.txt     # Python dependencies

Sample Input
- Brand: Hyundai
- Year: 2017
- Mileage: 45,000 km
- Fuel Type: Petrol
- Transmission: Manual
Predicted Price: ₹4.8 Lakhs

Future Improvements
- Add model comparison (Linear, Ridge, XGBoost)
- Integrate MongoDB for storing user queries
- Add Power BI dashboard for insights



