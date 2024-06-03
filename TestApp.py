import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit App Example")

st.header("Input Section")
# name = st.text_input("Enter your name:")

col1, spacer, col2 = st.columns([1, 0.25, 1])

with col1:
    regionidzip = st.number_input("Zip Code", value=95982, min_value=95982, max_value=97344)
    yearbuilt = st.number_input("Construction Year", value=1965, min_value=1808, max_value=2016)
    calculatedfinishedsquarefeet = st.number_input("Total Living Area in ft²", value=2000, min_value=1, max_value=183444)
    lotsizessquarefeet = st.number_input("Total Living Area in ft²", value=7000, min_value=169, max_value=14043439)
    bedroomcnt = st.slider("Number of Bedrooms", 0, 10, 3)
    roomcnt = st.slider("Total Room Count", 0, 10, 3)
    bathroomcnt = st.slider("Number of Bathrooms", 0, 6, 2)
    numberofstories = st.selectbox("Stories",("1","2"))  

with col2:
    unitcnt = st.selectbox(" Number of units the structure is built into (i.e. 2 = duplex, 3 = triplex, etc...)",("1","2","3","4","5","6","7"))
    fl_garage = st.checkbox("Garage", value=True)
    if fl_garage:
        garagecarcnt = st.selectbox("Number of garages on lot",("1","2","3","4","5"))
        garagetotalsqft = st.slider("Garage Area in ft²", value=100, min_value=0, max_value=1514)
    else:
        garagecarcnt = 0
        garagetotalsqft = 0
    
    fl_pool = st.checkbox("Pool", value=True)
    if fl_pool:
        poolsizesum = st.slider("Pool Area in ft²", value=400, min_value=19, max_value=2576)
    else:
        poolsizesum = 0

    fl_patio = st.checkbox("Patio", value=True)
    if fl_patio:
        yardbuildingsqft17 = st.slider("Patio Area in ft²", value=50, min_value=11, max_value=6407)
    else:
        yardbuildingsqft17 = 0

    fl_fireplace = st.checkbox("Fireplace", value=True)
    if fl_fireplace:
        fireplacecnt = st.selectbox("Fireplace Count",("1","2"))
    else:
        fireplacecnt = 0

                       
if st.button("Submit"):
    st.write(f"Hello, {name}. You are {age} years old.")

st.header("Data Section")
data = pd.DataFrame({
    'Column A': np.random.rand(100),
    'Column B': np.random.rand(100)

})
st.write("Here is a sample dataframe:")
st.dataframe(data)


