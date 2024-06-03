import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit App Example")

st.header("Input Section")
# name = st.text_input("Enter your name:")
yearbuilt = st.slider("Construction Year:", 1808, 2016, 2000)
bedroomnum = st.slider("Number of Bedrooms", 1, 10, 3)
bedroomnum = st.slider("Number of Bedrooms", 1, 10, 3)

locality = st.selectbox("Locality",("Aalst","Antwerp",))

if st.button("Submit"):
    st.write(f"Hello, {name}. You are {age} years old.")

st.header("Data Section")
data = pd.DataFrame({
    'Column A': np.random.rand(100),
    'Column B': np.random.rand(100)

})
st.write("Here is a sample dataframe:")
st.dataframe(data)


