import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Carregar CSV
df = pd.read_csv("ecommerce_preparados.csv")

# Padronizar dados de gênero
df['Gênero'] = df['Gênero'].str.lower().str.strip()
mapping = {
    'feminino': 'Feminino', 'mulher': 'Feminino',
    'meninas': 'Feminino','infantil feminino': 'Feminino',

    'masculino': 'Masculino', 'meninos': 'Masculino',
    'infantil masculino': 'Masculino',

    'sem gênero': 'Não definido', 'não definido': 'Não definido',
    'bebês': 'Não definido', 'bebe': 'Não definido'
}
df['Gênero'] = df['Gênero'].map(mapping).fillna('Não definido')

# HISTOGRAMA – Distribuição das Notas
plt.figure(figsize=(10,6))
plt.hist(df['Nota'], bins=50)
plt.title('Distribuição das Notas dos Produtos')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.show()
# ===========================

# DISPERSÃO – Preço vs Quantidade Vendida
plt.figure(figsize=(10,6))
plt.scatter(df['Preço'], df['Qtd_Vendidos_Cod'])
plt.title('Relação entre Preço e Quantidade Vendida')
plt.xlabel('Preço')
plt.ylabel('Quantidade Vendida')
plt.show()
# ===========================

#  MAPA DE CALOR – Correlação das variáveis
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, fmt=".2f", cmap="coolwarm")
plt.title('Mapa de Calor das Correlações')
plt.show()
# ===========================

# BARRA – Top 10 Marcas que Mais Vendem
top10_marcas = df.groupby('Marca')['Qtd_Vendidos_Cod'].sum().sort_values(ascending=False).head(9)

plt.figure(figsize=(12,6))
plt.bar(top10_marcas.index, top10_marcas.values)
plt.title('Top 10 Marcas por Quantidade Vendida')
plt.xlabel('Marca')
plt.ylabel('Quantidade Vendida')
plt.xticks(rotation=45)
plt.show()
# ===========================

# PIZZA – Divisão de Vendas por Gênero
xy = df.groupby('Gênero')['Qtd_Vendidos_Cod'].sum()

cores = {
    'Feminino': '#87cefa',
    'Masculino': '#afeeee',
    'Não definido': '#b8cad4'
}

plt.figure(figsize=(10,6))
plt.pie(xy.values, labels=xy.index, autopct='%1.1f%%',
        startangle=90, colors=[cores[g] for g in xy.index])
plt.title('Proporção de Vendas por Gênero')
plt.show()
# ===========================

# GRÁFICO DE DENSIDADE – Distribuição de Preço
plt.figure(figsize=(10,6))
sns.kdeplot(df['Preço'], fill=True, color='green')
plt.title('Densidade de Preço dos Produtos')
plt.xlabel('Preço')
plt.show()
# ===========================

# REGRESSÃO – Nota vs Número de Avaliações
plt.figure(figsize=(10,6))
sns.regplot(x='N_Avaliações', y='Nota', data= df, color='red', scatter_kws={'alpha': 0.8, 'color': 'green'})
plt.title('Relação entre Número de Avaliações e Nota Final')
plt.xlabel('Número de Avaliações')
plt.ylabel('Nota')
plt.show()
# ===========================