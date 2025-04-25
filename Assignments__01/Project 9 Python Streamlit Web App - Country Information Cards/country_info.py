import streamlit as st
import requests

st.title("Country Information Cards")

# Get list of countries from API
@st.cache_data
def get_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to load countries")
        return []

countries = get_countries()

# Prepare a list of country names sorted
country_names = sorted([country['name']['common'] for country in countries])

# Select country dropdown
selected_country = st.selectbox("Select a country", country_names)

# Find selected country info
def get_country_info(name):
    for country in countries:
        if country['name']['common'] == name:
            return country
    return None

country_info = get_country_info(selected_country)

if country_info:
    st.image(country_info['flags']['png'], width=150)
    st.header(country_info['name']['common'])
    st.write(f"**Capital:** {country_info.get('capital', ['N/A'])[0]}")
    st.write(f"**Region:** {country_info.get('region', 'N/A')}")
    st.write(f"**Population:** {country_info.get('population', 'N/A')}")
    st.write(f"**Area:** {country_info.get('area', 'N/A')} sq. km")
    st.write(f"**Languages:** {', '.join(country_info.get('languages', {}).values())}")
else:
    st.write("Country info not found.")
