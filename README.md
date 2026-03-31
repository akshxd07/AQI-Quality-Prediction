# Air Quality Index (AQI) Predictor

A machine learning web app that predicts Air Quality Index based on pollutant levels.

🔗 **Live Demo:** https://aqi-quality-prediction-eznnwpgdazwygds3ababak.streamlit.app

## Overview
Predicts AQI values using key environmental pollutants and classifies air quality
from Good to Severe using a trained Random Forest model.

## Features
- Real-time AQI prediction from pollutant inputs
- Air quality classification with severity levels
- Clean two-column UI built with Streamlit

## Tech Stack
- Python, Pandas, NumPy, Scikit-learn
- Random Forest Regression
- Streamlit (deployment)

## Model Performance
- R² Score: 0.88 on test data

## Input Features
PM2.5, PM10, NO₂, SO₂, CO, O₃, Temperature, Humidity

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Author
Akshad Yadav — [LinkedIn](https://linkedin.com/in/akshad-yadav-360724374) | [GitHub](https://github.com/akshxd07)
