import streamlit as st
import pickle
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ========== Custom Styling ==========
st.set_page_config(page_title="💻Laptop Price Predictor", layout="centered")
st.markdown("""
<style>
    .main {
        background-color: #f5f7fa;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        font-weight: bold;
        transition: background-color 0.3s;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
</style>
""", unsafe_allow_html=True)

# ========== Load Model and Data ==========
@st.cache_data
def load_data():
    return pickle.load(open('data.pkl', 'rb'))

@st.cache_data
def load_model():
    return pickle.load(open('pipe.pkl', 'rb'))

data = load_data()
pipe = load_model()

# ========== App Title ==========
st.title("💻 Laptop Price Predictor 💰")
st.markdown("Use this app to predict the price of a laptop based on its specifications. Fill out the form below and hit **Predict**!")

# ========== Input Columns ==========
col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox('Brand', data['Company'].unique())
    type = st.selectbox('Type', data['TypeName'].unique())
    Ram = st.selectbox('RAM (in GB)', [2, 4, 6, 8, 12, 16, 24, 32, 64])
    Touchscreen = st.selectbox('Touchscreen', ['No', 'Yes'])
    IPS = st.selectbox('IPS Panel', ['No', 'Yes'])
    resolution = st.selectbox('Screen Resolution', [
        "1280 x 800", "1366 x 768", "1920 x 1080", "2560 x 1440",
        "3200 x 1800", "2560 x 1600", "3072 x 1920", "3840 x 2160", "5120 x 2880"
    ])

with col2:
    Weight = st.number_input('Weight of the laptop (in kg)')
    screen_size = st.number_input('Screen Size (in inches)', min_value=0.1)
    cpu_brand = st.selectbox('CPU Brand', data['cpu_brand'].unique())
    HDD = st.selectbox('HDD (in GB)', [0, 128, 256, 512, 1024, 2048])
    SSD = st.selectbox('SSD (in GB)', [0, 8, 128, 256, 512, 1024])
    Gpu_brand = st.selectbox('GPU Brand', data['Gpu_brand'].unique())
    OS = st.selectbox('Operating System', data['OS'].unique())

# ========== Predict Button ==========
if st.button('🎯 Predict Price'):
    with st.spinner('Analyzing laptop specifications...'):
        # Convert features
        Touchscreen = 1 if Touchscreen == 'Yes' else 0
        IPS = 1 if IPS == 'Yes' else 0
        x_res, y_res = map(int, resolution.split(' x '))
        ppi = ((x_res ** 2 + y_res ** 2) ** 0.5) / screen_size

        # Model input
        query = np.array([brand, type, Ram, Weight, Touchscreen, IPS, ppi,
                          cpu_brand, HDD, SSD, Gpu_brand, OS]).reshape(1, -1)

        # Predict and display
        predicted_price = int(np.exp(pipe.predict(query)[0]))
        st.success(f"🎉 Predicted Price: **{predicted_price:,} PKR**")

# ========== Optional: Data Insights ==========
st.subheader("📊 Average Laptop Prices by Brand (Sample Data)")
avg_price_by_brand = data.groupby('Company')['Price'].mean().sort_values()

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x=avg_price_by_brand.values, y=avg_price_by_brand.index, palette='coolwarm', ax=ax)
ax.set_xlabel("Average Price")
ax.set_ylabel("Brand")
st.pyplot(fig)
