

A machine learning-powered Streamlit web app that predicts laptop prices based on specifications like brand, RAM, storage, screen resolution, CPU, and more. Built with Python and a trained regression model.Add commentMore actions

![Streamlit](https://img.shields.io/badge/Streamlit-Enabled-brightgreen?logo=streamlit)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-blue.svg)

---

## 🚀 Features

- 📦 Predict laptop prices in PKR using real-world data
- 🔍 User-friendly form to input specifications
- 🎯 Uses screen resolution to calculate PPI for accurate predictions
- 💡 Visual insights into average prices by brand
- 🎨 Light and dark themes with polished UI using custom CSS
- 🧠 Powered by a trained regression pipeline

---

## 🧰 Tech Stack

- **Python**
- **Streamlit**
- **NumPy / Pandas**
- **Scikit-learn**
- **Matplotlib & Seaborn**
- **Pickle** (for model and data storage)

---

## 📂 Project Structure

laptop-price-predictor/
├── index.py # Main Streamlit app
├── data.pkl # Preprocessed dataset
├── pipe.pkl # Trained ML model
├── requirements.txt # Python dependencies
└── .streamlit/
└── config.toml # UI theme settings

---

## ⚙️ Getting Started

### 1. Clone the Repository

bash
git clone https://github.com/your-username/laptop-price-predictor.git
cd laptop-price-predictor

## 🧠 Model Details
The model uses a log-transformed price regression and considers:

Brand

Laptop type

RAM, Weight

Touchscreen & IPS Panel (binary)

PPI (calculated from screen size and resolution)

Storage (HDD & SSD)

GPU and Operating System

## 🖼️ Demo

🔗 [https://laptop-price-prediction-ksregbmsojapp3bpfeuygp7.streamlit.app/]

## 🙌 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.
Add comment
