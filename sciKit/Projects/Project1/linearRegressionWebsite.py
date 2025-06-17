import numpy as np
import streamlit as st
import pandas as pd
import sklearn
import pickle
import os


from pyexpat import features
from streamlit import radio

model_path = os.path.join(os.path.dirname(__file__), 'Linear_regression_model.pkl')

model = pickle.load(open(model_path, 'rb'))

#WebUI

st.title("Sci-Kit Linear Regression Model")
tv=st.text_input("Enter TV sales...")
radio=st.text_input("Enter Radio sales...")
newspaper=st.text_input("Enter newspaper sales...")

if st.button("Predict"):
    features=np.array([[tv,radio,newspaper]],dtype=np.float64)
    results=model.predict(features).reshape(1,-1)
    st.write("Predicted sale ::::",results[0])
