import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head(20).to_string())

# Gráfico de Barras
plt.figure(figsize = (10,6))
