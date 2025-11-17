import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head().to_string())

# Grafico de Dispersão
sns.jointplot(x='idade', y='salario', data=df, kind='scatter') # ['scatter', 'hex', 'kde', 'reg', 'resid']
plt.show()

# Grafico de Densidade
plt.figure(figsize = (10,6))
sns.kdeplot(df['salario'], fill=True, color='pink')
plt.title('Densidade de Salários')
plt.xlabel('Salario')
plt.show()

# Grafico de Pairplot - Dispersão e Histograma
sns.pairplot(df[['idade', 'salario', 'anos_experiencia', 'nivel_educacao']]) # https://seaborn.pydata.org/tutorial/color_palettes.html
plt.show()

# Grafico de Regressão
sns.regplot(x='idade', y='salario', data=df, color='black', scatter_kws={'alpha': 0.5, 'color': 'green'})
plt.title('Regrassão de Salario por idade')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.show()

# Grafico countplot com hue
sns.countplot(x='estado_civil', hue='nivel_educacao', data=df, palette='pastel')
plt.xlabel('Estado Civil')
plt.ylabel('Nivel Educacao')
plt.legend(title='Nivel de Educacao')
plt.show()