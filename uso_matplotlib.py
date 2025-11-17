import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('clientes-v3-preparado.csv')
print(df.head(20).to_string())

# Gráfico de Barras
plt.figure(figsize = (10,6))                                         # link de Referencia
df['nivel_educacao'].value_counts().plot(kind='bar',color = 'green') # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas
plt.title('Divisão de Escolaridade -1')
plt.xlabel('Nivel de Educação')
plt.ylabel('Quantidade')
plt.xticks(rotation = 0)
plt.show()

x = df['nivel_educacao'].value_counts().index
y = df['nivel_educacao'].value_counts().values

plt.figure(figsize = (10,6))
plt.bar(x,y, color = 'red')
plt.title('Divisão de Escolaridade -2')
plt.xlabel('Nivel de Educacao')
plt.ylabel('Quantidade')
plt.show()

# Gráfico pizza
plt.figure(figsize = (10,6))
plt.pie(y, labels=x, autopct='%1.2f%%', startangle=90)
plt.title('Distribuição de nivel de Educacao')
plt.show()

# Gráfico de Dispersão                                                # link de Referencia
plt.hexbin(df['idade'], df['salario'], gridsize = 40, cmap = 'Blues') # https://matplotlib.org/stable/users/explain/colors/colormaps.html
plt.colorbar(label = 'contagem dentro do bin')
plt.xlabel('Idade')
plt.ylabel('Salario')
plt.title('Dispersão de Idade e Salário')
plt.show()