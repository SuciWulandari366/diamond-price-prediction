import streamlit as st
import joblib
import pandas as pd

# load model
model = joblib.load("model_diamond.pkl")

st.title("💎 Diamond Price Prediction")

st.write("Masukkan karakteristik diamond")

# input numerik
carat = st.number_input("Carat", 0.0, 5.0)
depth = st.number_input("Depth", 0.0, 100.0)
table = st.number_input("Table", 0.0, 100.0)
x = st.number_input("Length (x)", 0.0, 10.0)
y = st.number_input("Width (y)", 0.0, 10.0)
z = st.number_input("Height (z)", 0.0, 10.0)

# input kategori
cut = st.selectbox("Cut", ["Fair","Good","Very Good","Premium","Ideal"])
color = st.selectbox("Color", ["D","E","F","G","H","I","J"])
clarity = st.selectbox("Clarity", ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"])

if st.button("Predict Price"):

    # fitur numerik
    data = {
        "carat":[carat],
        "depth":[depth],
        "table":[table],
        "x":[x],
        "y":[y],
        "z":[z],
    }

    df = pd.DataFrame(data)

    # buat semua kolom dummy = 0
    dummy_cols = [
        'cut_Good','cut_Ideal','cut_Premium','cut_Very Good',
        'color_E','color_F','color_G','color_H','color_I','color_J',
        'clarity_IF','clarity_SI1','clarity_SI2','clarity_VS1',
        'clarity_VS2','clarity_VVS1','clarity_VVS2'
    ]

    for col in dummy_cols:
        df[col] = 0

    # isi dummy sesuai pilihan user
    if cut != "Fair":
        df[f"cut_{cut}"] = 1

    if color != "D":
        df[f"color_{color}"] = 1

    if clarity != "I1":
        df[f"clarity_{clarity}"] = 1

    # prediksi
    prediction = model.predict(df)

    st.success(f"💰 Predicted Price: ${prediction[0]:,.2f}")