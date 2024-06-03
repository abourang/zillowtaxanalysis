import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit App Example")

st.header("Input Section")
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 0, 100, 25)

if st.button("Submit"):
    st.write(f"Hello, {name}. You are {age} years old.")

st.header("Data Section")
data = pd.DataFrame({
    'Column A': np.random.rand(100),
    'Column B': np.random.rand(100)

    col1, spacer, col2 = st.columns([1, 0.25, 1])

with col1:
    subproperty_type_dict = {
        "APARTMENT": "Apartment",
        "HOUSE": "House",
        "APARTMENT_BLOCK": "Apartment Block",
        "BUNGALOW": "Bungalow",
        "CASTLE": "Castle",
        "CHALET": "Chalet",
        "COUNTRY_COTTAGE": "Country Cottage",
        "EXEPTIONAL_PROPERTY": "Exceptional Property",
        "DUPLEX": "Duplex",
        "FARMHOUSE": "Farmhouse",
        "FLAT_STUDIO": "Flat Studio",
        "GROUND_FLOOR": "Ground Floor",
        "LOFT": "Loft",
        "KOT": "Kot",
        "MANOR_HOUSE": "Manor House",
        "MANSION": "Mansion",
        "MIXED_USE_BUILDING": "Mixed Use Building",
        "PENTHOUSE": "Penthouse",
        "SERVICE_FLAT": "Service Flat",
        "TOWN_HOUSE": "Town House",
        "TRIPLEX": "Triplex",
        "VILLA": "Villa",
        "OTHER_PROPERTY": "Other Property",
    }

})
st.write("Here is a sample dataframe:")
st.dataframe(data)


