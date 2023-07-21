import pickle
import streamlit as st
from streamlit_option_menu import option_menu


diabetes_model = pickle.load(open("X:/Multiple diseases Prediction System/models/diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open("X:/Multiple diseases Prediction System/models/heart_model.sav", 'rb'))


with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction'],
                          icons=['activity','heart'],
                          default_index=0)


# Diabetes Prediction code    
    
if (selected == 'Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    
    col1, col2 = st.columns(2)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
    
    with col1:
        BloodPressure = st.text_input('Blood Pressure value')
    
    with col2:
        SkinThickness = st.text_input('Skin Thickness value')
    
    with col1:
        Insulin = st.text_input('Insulin Level')
    
    with col2:
        BMI = st.text_input('BMI value')
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    
    diab_diagnosis = ''
    

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if (diab_prediction[0] == 1):
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'     
    st.success(diab_diagnosis)



# Heart Disease Prediction code

if (selected == 'Heart Disease Prediction'):
    
    st.title('Heart Disease Prediction using ML')
    

    col1, col2 = st.columns(2)
    
    with col1:
        age = st.text_input('Age')
        
    with col2:
        sex = st.text_input('Sex')
        
    with col1:
        cp = st.text_input('Chest Pain types')
        
    with col2:
        trestbps = st.text_input('Resting Blood Pressure')
        
    with col1:
        chol = st.text_input('Serum Cholestoral')
        
    with col2:
        fbs = st.text_input('Fasting Blood Sugar')
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
        
    with col1:
        exang = st.text_input('Exercise Induced Angina')
        
    with col2:
        oldpeak = st.text_input('ST depression induced by exercise')
        
    with col1:
        slope = st.text_input('Slope of the peak exercise ST segment')
        
    with col2:
        ca = st.text_input('Major vessels colored by flourosopy')
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
        
 
    heart_diagnosis = ''
    
  
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])                          
        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'  
    st.success(heart_diagnosis)