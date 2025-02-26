import streamlit as st
import requests
from conversion_factors import conversion_factors  # Import your conversion data
import google.generativeai as genai
# API for real-time exchange rates
EXCHANGE_RATE_API = "https://api.exchangerate-api.com/v4/latest/USD"
genai.configure(api_key="AIzaSyBBTNFznyQOKaD56pYb-dXxwbp8bGYOXAI")
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
def convert_temperature(value, from_unit, to_unit):
    conversions = {
        ("Celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
        ("Celsius", "Kelvin"): lambda x: x + 273.15,
        ("Celsius", "Rankine"): lambda x: (x + 273.15) * 9/5,
        ("Celsius", "Delisle"): lambda x: (100 - x) * 1.5,
        ("Celsius", "Newton"): lambda x: x * 0.33,
        ("Celsius", "Réaumur"): lambda x: x * 0.8,
        ("Celsius", "Rømer"): lambda x: (x * 21/40) + 7.5,
        ("Fahrenheit", "Celsius"): lambda x: (x - 32) * 5/9,
        ("Fahrenheit", "Kelvin"): lambda x: (x - 32) * 5/9 + 273.15,
        ("Fahrenheit", "Rankine"): lambda x: x + 459.67,
        ("Kelvin", "Celsius"): lambda x: x - 273.15,
        ("Kelvin", "Fahrenheit"): lambda x: (x - 273.15) * 9/5 + 32,
        ("Kelvin", "Rankine"): lambda x: x * 9/5,
        ("Rankine", "Celsius"): lambda x: (x - 491.67) * 5/9,
        ("Rankine", "Fahrenheit"): lambda x: x - 459.67,
        ("Rankine", "Kelvin"): lambda x: x * 5/9
    }

    if (from_unit, to_unit) in conversions:
        return conversions[(from_unit, to_unit)](value)
    return None  # If conversion is not found

# Function to convert units
def convert_units(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value  # No conversion needed

    if from_unit in unit_categories["Temperature"] and to_unit in unit_categories["Temperature"]:
        return convert_temperature(value, from_unit, to_unit)

    if from_unit in currency_list and to_unit in currency_list:
        try:
            response = requests.get(EXCHANGE_RATE_API)
            data = response.json()
            rates = data["rates"]
            return value * (rates[to_unit] / rates[from_unit]) if from_unit in rates and to_unit in rates else None
        except Exception as e:
            st.error(f"Error fetching exchange rates: {e}")
            return None

    key = (from_unit, to_unit)
    reverse_key = (to_unit, from_unit)
    
    if key in conversion_factors:
        return value * conversion_factors[key]
    elif reverse_key in conversion_factors:
        return value / conversion_factors[reverse_key]

    return None  # Conversion not available

# Streamlit App UI
st.title("🌟 Advanced Unit Converter with Gemini AI 🤖")

# Unit conversion section
st.header("Unit Converter 🔄")
col1, col2 = st.columns(2)

with col1:
    value = st.number_input("Enter Value", min_value=0.0, format="%.4f")

with col2:
    category = st.selectbox("Select Category", list(unit_categories.keys()))

col3, col4 = st.columns(2)

with col3:
    from_unit = st.selectbox("From", unit_categories[category])

with col4:
    to_unit = st.selectbox("To", unit_categories[category])

if st.button("Convert 🔄"):
    result = convert_units(value, from_unit, to_unit)
    if result is not None:
        st.success(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")
    else:
        st.error("❌ Conversion not possible.")

# Ask Gemini AI Section
st.header("💬 Unit Converter")
user_prompt = st.text_area("Enter your question:", placeholder="Ask anything...")

def ask_gemini(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"❌ Error: {e}"

if st.button("Ask Unit🤖"):
    if user_prompt.strip():
        with st.spinner("Generating response..."):
            gemini_response = ask_gemini(user_prompt)
        st.success("✅ Response from Gemini:")
        st.write(gemini_response)
    else:
        st.warning("⚠️ Please enter a question before clicking the button.")    