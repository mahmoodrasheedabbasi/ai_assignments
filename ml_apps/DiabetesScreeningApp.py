import streamlit as st
import pickle

st.title("Diabetes Screening App")

def load_model():
    return pickle.load(open("diabetes_screening_model.pkl", "rb"))


check = st.checkbox("Load Model")

if check:
    model = load_model()
    st.info("Model Loaded Successfully")

    pregnancies = st.number_input("Enter Pregnancies", min_value= 0, max_value=17)
    glucose = st.number_input("Enter Glucose", min_value=0, max_value= 199)
    bloodPressure = st.number_input("Enter Blood Pressure", min_value=0, max_value=122)
    skinThickness = st.number_input("Enter Skin Thickness", min_value=0, max_value=99)
    insulin = st.number_input("Enter Insulin", min_value=0, max_value=846)
    bmi = st.number_input("Enter BMI", min_value= 0.0, max_value=67.1)
    diabetesPedigreeFunction = st.number_input("Enter Diabetes Pedigree Function", min_value=0.078, max_value=2.42)
    age = st.number_input("Enter Age", min_value=21, max_value=81)


    btn = st.button("Predict")

    if btn:
        result = model.predict([[pregnancies, glucose, bloodPressure,
                                skinThickness,insulin, bmi,
                                diabetesPedigreeFunction, age]])
        
        result = result[0]

        if result == 1:
            st.write("You are suffering from Diabetes, please take care and also contact to a doctor")
        else:
            st.write("You are not suffering from Diabetes")
