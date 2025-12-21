from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("aqi_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        pm25 = float(request.form['pm25'])
        pm10 = float(request.form['pm10'])
        no2 = float(request.form['no2'])
        so2 = float(request.form['so2'])
        co = float(request.form['co'])
        o3 = float(request.form['o3'])
        temp = float(request.form['temp'])
        humidity = float(request.form['humidity'])

        features = np.array([[pm25, pm10, no2, so2, co, o3, temp, humidity]])
        prediction = model.predict(features)[0]

        # Determine AQI Level
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

        result = f"Predicted AQI: {prediction:.2f} — {level}"

        return render_template('index.html', prediction_text=result, color=color)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}", color="black")

if __name__ == '__main__':
    app.run(debug=True)




