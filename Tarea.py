import pandas as pd


# Lee el archivo CSV
df = pd.read_csv('titanic.csv')

# Observa las primeras líneas
print(df.head())

# Obtén diferentes combinaciones de columnas y datos
print(df[['columna1', 'columna2']].head())  # Selecciona columnas específicas
print(df.loc[0:5, ['columna1', 'columna2']])  # Selecciona filas y columnas específicas
print(df.iloc[0:5, 0:2])  # Selecciona filas y columnas específicas por índice

# Revisa los datos obtenidos por la función describe
print(df.describe())
