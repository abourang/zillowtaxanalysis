import streamlit as st

horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; \
                        border: 1px solid #635985;'><br>"  # thin divider line

# Define the content of the Home page
# Display a logo and a title
st.image("streamlit/imgs/header.png")

with st.sidebar:
    st.image("streamlit/imgs/logo.png", width=100)  #

# st.sidebar.image("streamlit/imgs/logo.png", use_column_width=False)
st.title("Predicting House Value for Property Tax Assessment")
st.text("Zillow's Market Value Estimation")
st.text("BUS 48 Practical Analytics: Transforming Data into Decisions Stanford Continuing Studies")
st.markdown(horizontal_bar, True)
st.subheader("Business Problem")
st.markdown(
    """
    Background

      The property tax value assessment is a critical component for local governments, directly impacting revenue generation and public budgeting. Accurately predicting the tax value of houses is essential for municipalities and local governments to ensure equitable tax assessments and optimize revenue from property taxes. By leveraging data analytics and machine learning, it's possible to create a predictive model to improve the accuracy of these assessments, thereby ensuring fair taxation and optimized revenue. 

   Objectives
  
      To identify the key factors influencing the tax value of houses.
      Develop a predictive model that can forecast the tax value of houses accurately.
      Implement insights from the model to refine the assessment processes and ensure fair tax valuations.
"""
)
