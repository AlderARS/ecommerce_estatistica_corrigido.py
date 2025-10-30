import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# Carrega os dados
df = pd.read_csv("ecommerce_estatistica.csv")
lista_temp = df['Temporada'].unique()
opcoes = [{'label': temporada, 'value': temporada} for temporada in lista_temp]

# --- Funções dos gráficos ---
def graf_hist(df):
    fig = px.histogram(df, x='Nota')
    fig.update_layout(title='Aceitação dos Produtos',
                      xaxis_title='Nota',
                      yaxis_title='Contagem')
    return fig

def graf_disp(df):
    fig = px.scatter(df, x='Preço', y='Desconto')
    fig.update_layout(title='Desconto por Preço',
                      xaxis_title='Preço Produto',
                      yaxis_title='Desconto')
    return fig

def graf_calor(df):
    fig = px.density_heatmap(df, x='Desconto', y='N_Avaliações')
    fig.update_layout(title='Relação entre Campos:')
    return fig

def graf_barr(df):
    fig = px.bar(df, x='Gênero', y='Qtd_Vendidos_Cod')
    fig.update_layout(title='Vendas por Gênero',
                      xaxis_title='Gênero',
                      yaxis_title='Total de Vendas')
    return fig

def graf_pizza(df):
    fig = px.pie(df, names='Título', values='Qtd_Vendidos')
    fig.update_layout(title='Porcentagem de Vendas dos Produtos')
    return fig

def graf_densidade(df):
    fig = px.histogram(df, x='Título', y='Preço', histnorm='probability')
    fig.update_layout(title='Projeção de Valor dos Produtos',
                      xaxis_title='Produtos',
                      yaxis_title='Preço')
    return fig


# --- Criação do app ---
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Dashboard E-commerce"),
    dcc.Checklist(
        id='id_lista_temp',
        options=opcoes,
        value=[lista_temp[0]],
        inline=True
    ),
    dcc.Graph(id='id_graf_hist'),
    dcc.Graph(id='id_graf_disp'),
    dcc.Graph(id='id_graf_calor'),
    dcc.Graph(id='id_graf_barr'),
    dcc.Graph(id='id_graf_pizza'),
    dcc.Graph(id='id_graf_densidade'),
])


# --- Callback ---
@app.callback(
    [
        Output('id_graf_hist', 'figure'),
        Output('id_graf_disp', 'figure'),
        Output('id_graf_calor', 'figure'),
        Output('id_graf_barr', 'figure'),
        Output('id_graf_pizza', 'figure'),
        Output('id_graf_densidade', 'figure'),
    ],
    [Input('id_lista_temp', 'value')]
)
def update_figure(lista_temp):
    df_filtrado = df[df['Temporada'].isin(lista_temp)]

    fig1 = graf_hist(df_filtrado)
    fig2 = graf_disp(df_filtrado)
    fig3 = graf_calor(df_filtrado)
    fig4 = graf_barr(df_filtrado)
    fig5 = graf_pizza(df_filtrado)
    fig6 = graf_densidade(df_filtrado)

    return fig1, fig2, fig3, fig4, fig5, fig6


if __name__ == '__main__':
    app.run(debug=True, port=8050)
