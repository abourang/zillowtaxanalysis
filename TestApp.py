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
})
st.write("Here is a sample dataframe:")
st.dataframe(data)

    fl_garden = st.checkbox("Garden", value=True)
    if fl_garden:
        garden_sqm = st.slider(
            "Garden Area in m²", value=80, min_value=10, max_value=1000
