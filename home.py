import streamlit as st

horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; \
                        border: 1px solid #635985;'><br>"  # thin divider line

# Define the content of the Home page
# Display a logo and a title
st.image("header.png")

# st.sidebar.image("streamlit/imgs/logo.png", use_column_width=False)
st.title("Predicting House Value for Property Tax Assessment")
st.text("Zillow's Market Value Estimation")
st.text("BUS 48 Practical Analytics: Transforming Data into Decisions Stanford Continuing Studies")
st.markdown(horizontal_bar, True)
st.subheader("Business Problem")
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

# Streamlit app title

st.markdown(
    "<h1 style='text-align: center;'>Tax Price Prediction</h1><br>",
    unsafe_allow_html=True,
)


# dataLocality = pd.read_csv("data/locality_zip_codes.csv") EDIT


# sylvan Order:

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

    switched_dict = {value: key for key, value in subproperty_type_dict.items()}

    subproperty_type_key = st.selectbox("Property Type", list(switched_dict.keys()))
    subproperty_type_value = switched_dict[subproperty_type_key]

    if subproperty_type_value in (
        "APARTMENT",
        "DUPLEX",
        "FLAT_STUDIO",
        "GROUND_FLOOR",
        "KOT",
        "LOFT",
        "PENTHOUSE",
        "SERVICE_FLAT",
        "TRIPLEX",
    ):
        property_type = "APARTMENT"
    else:
        property_type = "HOUSE"

    locality = st.selectbox(
        "Locality",
        (
            "Aalst",
            "Antwerp",
            "Arlon",
            "Ath",
            "Bastogne",
            "Brugge",
            "Brussels",
            "Charleroi",
            "Dendermonde",
            "Diksmuide",
            "Dinant",
            "Eeklo",
            "Gent",
            "Halle-Vilvoorde",
            "Hasselt",
            "Huy",
            "Ieper",
            "Kortrijk",
            "Leuven",
            "Liège",
            "Maaseik",
            "Marche-en-Famenne",
            "Mechelen",
            "Mons",
            "Mouscron",
            "Namur",
            "Neufchâteau",
            "Nivelles",
            "Oostend",
            "Oudenaarde",
            "Philippeville",
            "Roeselare",
            "Sint-Niklaas",
            "Soignies",
            "Thuin",
            "Tielt",
            "Tongeren",
            "Tournai",
            "Turnhout",
            "Verviers",
            "Veurne",
            "Virton",
            "Waremme",
        ),
    )
    if locality:
        data = dataLocality[dataLocality["locality"] == f"{locality}"]
        zip_code = st.selectbox("ZIP Code", data["zip_code"].to_list())
    construction_year = st.number_input(
        "Construction Year", value=2000, min_value=1808, max_value=2016
    )
    total_area_sqm = st.number_input(
        "Total Living Area in ft²", value=150, min_value=10, max_value=1000
    )
    epc = st.selectbox(
        "Fire Place Count",
        ("0", "1", "2"),
    )
    if epc == "Unknown":
        epc = "MISSING"

    equipped_kitchen = st.checkbox(
        "Is your kitchen equipped?",
    )
    state_building = st.checkbox(
        "Property renovated in the last 2 years?",
    )

with col2:
    nbr_roomcnt = st.slider("Number of Bedrooms", value=3, min_value=1, max_value=10)
    lotsizesquarefeet = st.slider(
        "Lot Size in ft²", value=1000, min_value=169, max_value=14043439
    )
    nbr_rooomcnt = st.slider("Number of Frontages", value=1, min_value=0, max_value=5)

    fl_terrace = st.checkbox("Terrace", value=True)
    if fl_terrace:
        terrace_sqm = st.slider(
            "Terrace Area in m²", value=20, min_value=10, max_value=100
        )
    else:
        terrace_sqm = 0
      
    fl_garagecarcnt = st.checkbox("Garage", value=True)
    if fl_garagecarcnt:
        garagecarcnt = st.slider(
            "Garden Area in m²", value=80, min_value=10, max_value=1000
          epc = st.selectbox(
        "Fire Place Count",
        ("0", "1", "2"),

        fl_garden = st.checkbox("Garden", value=True)
    if fl_garden:
        garden_sqm = st.slider(
            "Garden Area in m²", value=80, min_value=10, max_value=1000
        )
    else:
        garden_sqm = 0
    fl_swimming_pool = st.checkbox("Swimming Pool")
    fl_double_glazing = st.checkbox("Double Glazing")
    fl_open_fire = st.checkbox("Open Fire")

