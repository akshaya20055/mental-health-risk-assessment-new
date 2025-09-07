# mental-health-prediction-based-on-pm2.5-pollutant
This project predicts an individual's Mental Health Risk Score using two features: self-reported stress level and PM2.5 air pollution. A Linear Regression model is used to estimate how stress and pollution contribute to mental health risk.
MENTAL HEALTH RISK PREDICTION PROJECT

PM2.5 COMRE FROM ?
>Vehicle emissions
>Factory smoke
>Fires (wildfires, burning trash, etc.)
>Construction dust
>Coal/oil combustion

PROJECT OVERVIEW:
This project aims to predict an individual's Mental Health Risk Score based on two key factors:
•Self-Reported Stress Level: How stressed the person feels (on a scale, e.g., 1 to 10).
•PM2.5 (µg/m³): The concentration of fine particulate matter (air pollution) in micrograms per cubic meter where the individual resides.
The goal is to build a machine learning model that can accurately estimate the mental health risk score from these two features. This risk score helps in understanding how stress and environmental factors like air pollution might affect mental well-being.

DATASET DESCRIPTION:
The dataset (mental_health_risk_data.csv) contains 200 rows with the following columns:
Feature: Description
PM2.5 (µg/m³): Fine particulate air pollution concentration, measured in micrograms per cubic meter (µg/m³). High values indicate more polluted air.
Self_Reported_Stress_Level: A subjective measure of how stressed an individual feels, typically on a scale from 1 (low stress) to 10 (high stress).
Mental_Health_Risk_Score: The target variable, representing the estimated risk of mental health problems. Values range roughly from 0 to 1, where higher scores indicate greater risk.

MACHINE LEARNING PREDICTION PROCESS:
The project follows a standard machine learning workflow divided into several key stages:
1.Data Loading & Understanding
The dataset is loaded into the program using pandas.
Initial data visualization helps understand relationships between stress, pollution, and mental health risk. For example, scatter plots show how risk scores relate to stress levels and PM2.5.
2.Data Preparation
Two columns, Self_Reported_Stress_Level and PM2.5, are selected as input features.
The target variable is Mental_Health_Risk_Score.
The dataset is split into:
Training data (80%): Used to train the model.
Testing data (20%): Used to evaluate how well the model learned.
3.Model Training
A Linear Regression model is trained on the training data.
Linear Regression fits a line (or hyperplane in multiple features) to predict risk scores based on the input features.
4.Model Prediction
The trained model predicts mental health risk scores on the test data.
Predictions are continuous values estimating the risk score.
5.Evaluation
The model’s accuracy is evaluated using:
Mean Squared Error (MSE): Measures the average squared difference between actual and predicted risk scores. Lower values indicate better predictions.
Categorical Accuracy: Converts continuous risk scores into categories (No Risk, Low, Moderate, High) and measures how often predicted categories match actual categories.
Visualization tools like Actual vs. Predicted plots and Residual plots help visually assess model performance.
6.Deployment (Example Predictions)
The model can predict risk for new individuals by inputting their stress level and PM2.5 values.
I have included a small Flask app with a simple HTML interface to predict output in a GUI mode.
Predicted risk scores are also converted to categories for easier interpretation.

RISK CATEGORIES DEFINED:
Risk scores are divided into four categories for better understanding:
Score Range	Risk Category
0.00 – 0.25	No Risk
0.26 – 0.50	Low Risk
0.51 – 0.75	Moderate Risk
0.76 – 1.00	High Risk

SUMMARY OF RESULTS:
The model achieved an MSE of approximately 0.0008, indicating small errors in predictions.
The categorical accuracy was around 88%, meaning the model correctly predicted the risk category in most cases.
Example predictions show how different stress levels and pollution impact the predicted mental health risk score.

CONCLUSION:
This project demonstrates how simple environmental and psychological features can be used to predict mental health risk scores with reasonable accuracy. Visualizations help understand data and model behavior, and the model can be used for practical predictions.
Feel free to explore, improve, or extend this model with more features or complex algorithms.

NOTE:
If you want to run this project, make sure you have installed Jupyter Notebook, Python, and the Flask module on your machine. You will likely download this code, so you may need to update the file paths mentioned in the code to match your local paths.

