import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Load cleaned data
data = pd.read_csv('cleaned_nutrition_data.csv', sep=';')

# Fitur untuk rekomendasi
features = data[['Fat', 'Sugars', 'Protein', 'Calcium']]

# Latih model k-NN
model = NearestNeighbors(n_neighbors=10, metric='euclidean')
model.fit(features)

# Fungsi rekomendasi
def recommend(input_features):
    distances, indices = model.kneighbors([input_features])
    return data.iloc[indices[0]]

# Contoh penggunaan
# input_features = [20, 10, 130, 2000]  # Fat, Sugars, Protein, Calcium
# recommendations = recommend(input_features)
# print(recommendations)
