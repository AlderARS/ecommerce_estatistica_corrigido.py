import pandas as pd
import matplotlib as plt
import seaborn as sns

df = pd.read_csv("ecommerce.csv")

### Linhas e Colunas
print(df.shape, "\n")
### Cabeça e Cauda
print(df.head(), "\n")
print(df.tail(), "\n")
### Nome das Colunas
columns_list = df.columns.tolist()
print(columns_list, "\n")
### Typos de Dados por Coluna
print(df.dtypes, "\n")
### Resumo de Estatísticas
print(df.describe(), "\n")
### Itens Únicos em cada coluna
print(df[columns_list].nunique(), "\n")

### Gráfico de Histograma
def graf_hist(df):
    plt.subplot(3,3,1)
    plt.hist(df['Nota'])
    plt.title('Nota Geral dos Produtos')
    plt.xlabel('Nota')
    plt.ylabel('Contagem')


### Gráfico de dispersão
def graf_disp(df):
    plt.subplot(3,3,2)
    plt.scatter(df['Preço'], df['Desconto'])
    plt.ylabel('Desconto')
    plt.xlabel('Preço do Produto')
    plt.title('Desconto por Preço')

### Mapa de calor (Nota e N_avaliação)
def graf_calor(df):
    plt.subplot(3,3,3)
    corr = df[['Nota', 'Material_Cod', 'Desconto']].corr()
    sns.heatmap(corr, annot=True)
    plt.title('Relação entre Campos:')

### Gráfico de barra
def graf_barr(df):
    plt.subplot(3,3,4)
    df['Qtd_Vendidos'].value_counts().plot(kind='bar', title='Quantidade de Vendidos')
    plt.title('Qtd de Vendas dos Produtos')
    plt.xlabel('Qtd Vendas')
    plt.ylabel('Contagem')

### Gráfico de pizza (Porcentagem de Nota dos Produtos em Geral)
def graf_pizza(df):
    plt.subplot(3,3,5)
    df['Qtd_Vendidos'].value_counts().plot(kind='pie', title='Qtd Vendidos')
    plt.title('Porcentagem de Vendas dos Produtos')

### Gráfico de densidade (N_Avaliações)
def graf_densidade(df):
    plt.subplot(3,3,6)
    sns.kdeplot(df['Nota'], fill=True, color='#863e9c')
    plt.title('Avaliação de todos os produtos')
    plt.xlabel('Nota')
    plt.ylabel('Contagem')

### Gráfico de Regressão
def graf_regress(df):
    plt.subplot(3,3,7)
    sns.regplot(x='N_Avaliações', y='Desconto', data=df)
    plt.title('Projeção de Avaliações por Desconto')
    plt.xlabel('Avaliações')
    plt.ylabel('Desconto')


### Mostrando os Gráficos
def junta_graf(df):
    graf_hist(df)
    graf_disp(df)
    graf_calor(df)
    graf_barr(df)
    graf_pizz(df)
    graf_densid(df)
    graf_regress(df)

junta_graf(df)
plt.tight_layout()
plt.show()