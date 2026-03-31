import streamlit as st
import joblib
import numpy as np

model = joblib.load("aqi_model.pkl")

st.set_page_config(page_title="AQI Predictor", page_icon="🌿")
st.title("🌿 Air Quality Index Predictor")
st.markdown("Enter pollutant levels to predict the AQI and air quality category.")

col1, col2 = st.columns(2)

with col1:
    pm25 = st.number_input("PM2.5", min_value=0.0)
    pm10 = st.number_input("PM10", min_value=0.0)
    no2 = st.number_input("NO2", min_value=0.0)
    so2 = st.number_input("SO2", min_value=0.0)

with col2:
    co = st.number_input("CO", min_value=0.0)
    o3 = st.number_input("O3", min_value=0.0)
    temp = st.number_input("Temperature (°C)")
    humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0)

if st.button("Predict AQI"):
    features = np.array([[pm25, pm10, no2, so2, co, o3, temp, humidity]])
    prediction = model.predict(features)[0]

    if prediction <= 50:
        level = "Good 😊"
        color = "green"
    elif prediction <= 100:
        level = "Satisfactory 🙂"
        color = "limegreen"
    elif prediction <= 200:
        level = "Moderate 😐"
        color = "orange"
    elif prediction <= 300:
        level = "Poor 😷"
        color = "red"
    elif prediction <= 400:
        level = "Very Poor 😫"
        color = "purple"
    else:
        level = "Severe ☠️"
        color = "maroon"

    st.markdown(f"### Predicted AQI: `{prediction:.2f}`")
    st.markdown(f"**Air Quality: <span style='color:{color}'>{level}</span>**",
                unsafe_allow_html=True)