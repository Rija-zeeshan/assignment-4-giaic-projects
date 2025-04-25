import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App!")
st.write("Yeh app tumhe data dikhayega aur tumse interact karega.")

# Create random data
data = pd.DataFrame(
    np.random.randn(10, 3),
    columns=['A', 'B', 'C']
)

st.write("Random data table:")
st.dataframe(data)

# Simple chart
st.line_chart(data)

# User input example
number = st.slider("Select a number", 0, 100, 25)
st.write(f"You selected: {number}")

if st.button("Click me"):
    st.write("Button clicked! 🎉")
