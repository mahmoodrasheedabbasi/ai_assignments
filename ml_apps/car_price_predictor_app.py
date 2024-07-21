import streamlit as st
import pickle
import pandas as pd

st.title("Car Price Predictor")


def load_model():
    model = pickle.load(open('car_price_predictor.pkl', 'rb'))
    return model


check = st.checkbox("Load Model")


if check:
    model = load_model()
    st.warning("Model Loaded Successfully")
    
    df_clean = pd.read_csv("cleaned_car_data.csv")
    df_preprocess = pd.read_csv("preprocessed_car_data.csv")

    company_list = df_clean["company"].unique().tolist()


    company = st.selectbox("Select company", company_list)

    name_list = df_clean[df_clean["company"] == company]["name"].unique().tolist()

    name = st.selectbox("Select name", name_list)
    
    year_list = df_clean[df_clean["name"] == name]["year"].unique().tolist()

    year = st.selectbox("Enter year", year_list)

    kms_driven = st.number_input("Enter kilometers driven")
    
    fuel_type_list = df_clean[df_clean["name"] == name]["fuel_type"].unique().tolist()

    fuel_type = st.selectbox("Enter fuel type", fuel_type_list)


    btn =  st.button("Predict")


    # Data Preprocessing

    if btn:

        name_index = df_clean["name"].to_list().index(name)
        name_preprocessed = df_preprocess["name"].to_list()[name_index]
        
        company_index = df_clean["company"].to_list().index(company)
        company_preprocessed = df_preprocess["company"].to_list()[company_index]
        
        year_index = df_clean["year"].to_list().index(year)
        year_preprocessed = df_preprocess["year"].to_list()[year_index]

        if fuel_type == "Diesel":
            fuel_type = 0 
        elif fuel_type == "LPG":
            fuel_type = 1
        else:
            fuel_type = 2


        price = model.predict([[name_preprocessed, company_preprocessed, 
                                year_preprocessed, kms_driven, fuel_type]])
        price = price[0]
        st.info(f"Price = {int(price)}")