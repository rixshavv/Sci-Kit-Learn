from sklearn.preprocessing import LabelEncoder,StandardScaler
import pickle
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
import os
le = LabelEncoder()
scaler = StandardScaler()
lgr = LinearRegression()


#Loading model and data
model_path = os.path.join(os.path.dirname(__file__), 'lgr.pkl')

model = pickle.load(open(model_path, 'rb'))

#Title for website
st.title('Logistic Regression for Churn Prediction')
gender=st.selectbox('Select Gender:', options=['Yes=Male', 'No=Female'])
SeniorCitizen=st.selectbox('Select Citizenship:', options=['Yes', 'No'])
Partner = st.selectbox('Do you have partner?', options=['Yes','No'])
Dependents= st.selectbox('Are you dependents on other?', options=['Yes','No'])
tenure = st.text_input("Enter Your tenure?")
PhoneService = st. selectbox("Do have phone service?", options=['Yes','No'])
MultipleLines = st.selectbox("Do you have nutlilines servics?", options=['Yes','No','none'])
Contract = st.selectbox("Your Contracts?" ,options=['One year','Two year','Month-to_month'])
TotalCharges = st. text_input("Enter your Total charges?")


def predictive(gender, Seniorcitizen, Dependents, tenure, Phoneservice, multiline, contact, totalcharge):
        data = {
            'gender': [gender],
            'SeniorCitizen': [Seniorcitizen],
            'Partner': [Partner],
            "Dependents": [Dependents],
            'tenure': [tenure],
            "PhoneService": [Phoneservice],
            "MultipleLines": [multiline],
            'Contract': [contact],
            'TotalCharges': [totalcharge]
        }
        df1 = pd.DataFrame(data)

        categorical_cols = ['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'MultipleLines', 'Contract']
        for col in categorical_cols:
            df1[col] = le.fit_transform(df1[col])

        df1 = scaler.fit_transform(df1)
        result = lgr.predict(df1).reshape(1, -1)
        return result[0]

if st.button('Predict'):
    result = predictive(gender, SeniorCitizen, Dependents, tenure, PhoneService, MultipleLines, Contract, TotalCharges)
    if result == 0:
        print("Not Churn")
    else:
        print("Churn")





