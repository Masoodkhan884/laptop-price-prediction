import streamlit as st
import pickle
import numpy as np

# Load pre-trained model and data
data = pickle.load(open('data.pkl', 'rb'))
# Load the 'pipe' object (the model)
pipe = pickle.load(open('pipe.pkl', 'rb'))

st.title('Laptop Price Prediction')

# Select laptop brand
brand = st.selectbox('Brand', data['Company'].unique())

# Select laptop type
type = st.selectbox('Type', data['TypeName'].unique())

# Select RAM size
Ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])

# Input laptop weight
Weight = st.number_input('Weight of the laptop (in kg)')

# Select if the laptop has a touchscreen
Touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])

# Select if the laptop has an IPS panel
IPS = st.selectbox('IPS Panel', ['No', 'Yes'])

# Input screen size
screen_size = st.number_input('Screen Size (in inches)', min_value=0.1)

# Select screen resolution
resolution = st.selectbox('Screen Resolution', ["1280 x 800", "1366 x 768", "1920 x 1080", "2560 x 1440",
                            "3200 x 1800", "2560 x 1600", "3072 x 1920", "3840 x 2160", "5120 x 2880"])

# Select CPU brand
cpu_brand = st.selectbox('CPU Brand', data['cpu_brand'].unique())

# Select HDD size
HDD = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])

# Select SSD size
SSD = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])

# Select GPU brand
Gpu_brand = st.selectbox('GPU Brand', data['Gpu_brand'].unique())

# Select Operating System
OS = st.selectbox('Operating System', data['OS'].unique())

# Predict price on button click
if st.button('Predict Price'):
    # Convert touchscreen and IPS values to binary
    Touchscreen = 1 if Touchscreen == 'Yes' else 0
    IPS = 1 if IPS == 'Yes' else 0

    # Process screen resolution to calculate pixels per inch (ppi)
    x_res, y_res = map(int, resolution.split(' x '))
    ppi = ((x_res ** 2 + y_res ** 2) ** 0.5) / screen_size

    # Create input query for the model
    Query = np.array([brand, type, Ram, Weight, Touchscreen, IPS, ppi, cpu_brand, HDD, SSD, Gpu_brand, OS])
    Query = Query.reshape(1, -1)

    # Predict price and display result
    predicted_price = int(np.exp(pipe.predict(Query)[0]))
    st.title(f"Predicted Price  :  {predicted_price}   pkr")
