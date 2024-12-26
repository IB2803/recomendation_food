import pandas as pd

# Load data
data = pd.read_csv('Dataset_Nutrition.csv')

# Tampilkan 5 baris pertama sebelum pembersihan
print("Sebelum Pembersihan Data:")
print(data.head())

# Lihat informasi dataset
print(data.head())

# Bersihkan data (contoh: hilangkan kolom kosong)
data_clean = data.dropna()
data_clean = data.drop_duplicates()
# Periksa ukuran data setelah pembersihan
print("\nSetelah Pembersihan Data:")
print(data_clean.head())
# Simpan data bersih
data_clean.to_csv('cleaned_nutrition_data.csv', index=False)

print("\nData bersih berhasil disimpan dalam 'cleaned_nutrition_data.csv'")