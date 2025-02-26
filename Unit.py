import streamlit as st
import requests
from conversion_factors import conversion_factors  # Import your conversion data

# API for real-time exchange rates
EXCHANGE_RATE_API = "https://api.exchangerate-api.com/v4/latest/USD"

# Function to fetch all available currencies
def fetch_currencies():
    try:
        response = requests.get(EXCHANGE_RATE_API)
        data = response.json()
        return list(data["rates"].keys())  # Get all currency codes
    except Exception as e:
        st.error(f"Error fetching currency list: {e}")
        return ["USD", "EUR", "GBP"]  # Fallback currencies

# Fetch all currencies dynamically
currency_list = fetch_currencies()

# Categorizing units
unit_categories = {
    "Length": ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches", "Nautical Miles", "Light Years", "Micrometers", "Nanometers"],
    "Weight": ["Milligrams", "Grams", "Kilograms", "Metric Tons", "Pounds", "Ounces", "Stones", "Carats", "Grains", "Long Tons (UK)", "Short Tons (US)"],
    "Volume": ["Liters", "Milliliters", "Cubic Meters", "Cubic Centimeters", "Cubic Millimeters", "Cubic Inches", "Cubic Feet", "Cubic Yards", "Gallons (US)", "Gallons (UK)", "Quarts (US)", "Quarts (UK)", "Pints (US)", "Pints (UK)", "Fluid Ounces (US)", "Fluid Ounces (UK)", "Cups (US)", "Cups (UK)", "Tablespoons (US)", "Tablespoons (UK)", "Teaspoons (US)", "Teaspoons (UK)"],
    "Temperature": ["Celsius", "Fahrenheit", "Kelvin", "Rankine", "Delisle", "Newton", "Réaumur", "Rømer"],
    "Time": ["Seconds", "Minutes", "Hours", "Days", "Weeks", "Months", "Years", "Decades", "Centuries", "Millennia"],
    "Speed": ["Meters per Second", "Kilometers per Hour", "Miles per Hour", "Knots", "Feet per Second"],
    "Area": ["Square Meters", "Square Kilometers", "Square Centimeters", "Square Millimeters", "Square Inches",
             "Square Feet", "Square Yards", "Square Miles", "Acres", "Hectares"],
    "Pressure": ["Pascals", "Kilopascals", "Megapascals", "Bars", "Atmospheres", "Millimeters of Mercury",
                 "Inches of Mercury"],
    "Power": ["Watts", "Kilowatts", "Megawatts", "Horsepower"],
    "Energy": ["Joules", "Kilojoules", "Calories", "Kilocalories", "Electronvolts", "BTU"],
    "Currency": currency_list,  # Dynamically fetched list
}

# Function to convert units
def convert_units(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value  # No conversion needed

    # Handle currency conversion separately
    if from_unit in currency_list and to_unit in currency_list:
        try:
            response = requests.get(EXCHANGE_RATE_API)
            data = response.json()
            rates = data["rates"]
            
            if from_unit in rates and to_unit in rates:
                return value * (rates[to_unit] / rates[from_unit])
            else:
                return None
        except Exception as e:
            st.error(f"Error fetching exchange rates: {e}")
            return None

    # General unit conversion
    key = (from_unit, to_unit)
    reverse_key = (to_unit, from_unit)

    if key in conversion_factors:
        return value * conversion_factors[key]
    elif reverse_key in conversion_factors:
        return value / conversion_factors[reverse_key]

    return None  # Conversion not available

# Custom CSS for styling
st.markdown("""
    <style>
        .stTextInput>div>div>input {
            font-size: 18px !important;
            padding: 10px;
        }
        .stSelectbox>div>div {
            font-size: 18px !important;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            font-size: 18px;
            border-radius: 8px;
            display: flex;
            margin: auto;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit app
st.title("🌟 Advanced Unit Converter")

# Two columns for input fields in one row
col1, col2 = st.columns(2)

with col1:
    value = st.number_input("Enter Value", min_value=0.0, format="%.4f")

with col2:
    category = st.selectbox("Select Category", list(unit_categories.keys()))

# Two columns for unit selection in one row
col3, col4 = st.columns(2)

with col3:
    from_unit = st.selectbox("From", unit_categories[category])

with col4:
    to_unit = st.selectbox("To", unit_categories[category])

# Convert and display result
if st.button("Convert 🔄"):
    result = convert_units(value, from_unit, to_unit)
    if result is not None:
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")
    else:
        st.error("❌ Conversion not possible.")
