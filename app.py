from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load dataset and train model once when app starts
data = pd.read_csv(
    r"C:\Users\userd\Mental_Health_Risk\mental_health_risk_data.csv",
    encoding='latin1'
)
X = data[['Self_Reported_Stress_Level', 'PM2.5 (µg/m³)']]
y = data['Mental_Health_Risk_Score']
model = LinearRegression().fit(X, y)

# Function to convert risk score into categories
def categorize_risk(score):
    if score <= 0.25:
        return 'No Risk'
    elif score <= 0.5:
        return 'Low Risk'
    elif score <= 0.75:
        return 'Moderate Risk'
    else:
        return 'High Risk'

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    stress = float(request.form['stress_level'])
    pm25 = float(request.form['pm25'])

    df = pd.DataFrame(
        [[stress, pm25]],
        columns=['Self_Reported_Stress_Level', 'PM2.5 (µg/m³)']
    )
    score = model.predict(df)[0]
    category = categorize_risk(score)

    return render_template(
        'index.html',
        prediction_text=f"Predicted Risk Score: {score:.3f}",
        risk_category=f"Risk Category: {category}"
    )

if __name__ == '__main__':
    app.run(debug=True)
