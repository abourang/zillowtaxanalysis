import streamlit as st
import pandas as pd
import numpy as np

st.title("Streamlit App Example")

horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; \
                        border: 1px solid #635985;'><br>"  # thin divider line

# Define the content of the Home page
# Display a logo and a title
st.image("header.png")

# st.sidebar.image("streamlit/imgs/logo.png", use_column_width=False)
st.title("Predicting House Value for Property Tax Assessment")
st.text("BUS 48 Practical Analytics: Transforming Data into Decisions")
st.markdown(horizontal_bar, True)
st.subheader("Zillow's Market Value Estimation")
st.markdown(
    """
    **Background**
    
      The property tax value assessment is a critical component for local governments, directly impacting revenue generation and public budgeting. Accurately predicting the tax value of houses is essential for municipalities and local governments to ensure equitable tax assessments and optimize revenue from property taxes. By leveraging data analytics and machine learning, it's possible to create a predictive model to improve the accuracy of these assessments, thereby ensuring fair taxation and optimized revenue. 

   **Objectives**
   
      To identify the key factors influencing the tax value of houses.
      
      Develop a predictive model that can forecast the tax value of houses accurately.
      
      Implement insights from the model to refine the assessment processes and ensure fair tax valuations.
      
"""
)

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
    unitcnt = st.selectbox(" Number of units)",("1","2","3","4","5","6","7"))
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


