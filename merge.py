import pandas as pd

# List semua file CSV
files = ["data1.csv", "data2.csv", "data3.csv", "data4.csv", "data5.csv"]

# Gabungkan semua file
combined_data = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)

# Simpan ke file CSV baru
combined_data.to_csv("combined_data.csv", index=False)

print("Data berhasil digabung!")
