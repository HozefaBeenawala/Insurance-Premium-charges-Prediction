import streamlit as st
import numpy as np
import pickle
import pandas as pd
from PIL import Image
import json

pkl = open('insurance_charges_prediction_model.pickle','rb')
regressor = pickle.load(pkl)

def welcome():
    return "Welcome All"

with open('all_columns.json') as f:
        all_columns = json.load(f)
        print(all_columns.values())
columns_list = []
for i in all_columns.values():
    columns_list.append(i)
    print(columns_list)
from itertools import chain
all_columns_list = list(chain(*columns_list))
print(all_columns_list)

def predict_charges (age, sex, bmi, children, smoker, region):
    loc_index = np.where(all_columns_list==region)[0][0]
    
    x = np.zeros(len(all_columns_list))
    x[0] = age
    x[1] = sex
    x[2] = bmi
    x[3] = children
    x[4] = smoker
    if loc_index >= 0:
        x[loc_index] = 1
    
    prediction=regressor.predict([x])[0]
    print(prediction)
    return prediction
    #prediction=regressor.predict ([[age, sex, bmi, children, smoker, region]])
    #print(prediction)
    #return prediction

def main():
    st.title("Insurance Premium Charges ML App")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Energy Efficiency Prediction</h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    age = st.text_input("Age")
    sex = st.text_input("Sex")
    bmi = st.text_input("BMI")
    children = st.text_input("Children")
    smoker = st.text_input("Smoker")
    with open('columns.json') as f:
        Region = json.load(f)
        print(Region.values())
    l = []
    for i in Region.values():
        l.append(i)
        print(l)
    Region_list = list(chain(*l))
    print(Region_list)
    region = st.selectbox('Select a Region', Region_list)
    
    result = ""
    
    if st.button("Predict Premium Charges"):
        result=predict_charges (age, sex, bmi, children, smoker, region)
    st.success('The output is (in Rs) {}'.format(result))
    
    if st.button("About"):
        st.text("This is a Insurance Premium Charges Prediction app which is used to predict insurance premium charges.")

if __name__=='__main__' :
    main()