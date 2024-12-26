import streamlit as st
import pandas as pd
from model import recommend  # Pastikan file model.py ada di direktori yang sama

# Judul aplikasi
st.title("Sistem Rekomendasi Nutrisi Berbasis Gaya Hidup")

# Pilih parameter yang ingin diinputkan
st.header("Pilih Data Nutrisi")
parameters = st.multiselect(
    "Pilih Nutrisi yang ingin diinputkan",
    ['Fat', 'Sugars', 'Protein', 'Calcium']
)

# Siapkan variabel input
fat = 0.0
sugars = 0.0
protein = 0.0
calcium = 0.0

# Input data berdasarkan pilihan
if 'Fat' in parameters:
    fat = st.number_input("Fat (gram)", min_value=0.0, step=0.1)
if 'Sugars' in parameters:
    sugars = st.number_input("Sugars (gram)", min_value=0.0, step=0.1)
if 'Protein' in parameters:
    protein = st.number_input("Protein (gram)", min_value=0.0, step=0.1)
if 'Calcium' in parameters:
    calcium = st.number_input("Calcium (mg)", min_value=0.0, step=0.1)

# Tombol untuk memproses
if st.button("Rekomendasikan Nutrisi"):
    # Siapkan data input
    input_features = [fat, sugars, protein, calcium]
    try:
        # Panggil fungsi rekomendasi dari model
        results = recommend(input_features)
        # Tampilkan hasil rekomendasi
        st.header("Hasil Rekomendasi")
        st.dataframe(results)
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
