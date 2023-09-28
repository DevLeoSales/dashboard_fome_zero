import streamlit as st
import pandas as pd
import inflection
import plotly.express as px

st.set_page_config(
    page_title="Main Page",
    page_icon="📊",
    layout='wide'
)

# Leitura dos dados
df = pd.read_csv('dataset/zomato.csv')
df1 = df.copy()

# Tratamento dos dados
# Renomear as colunas
def rename_columns(dataframe):
    df = dataframe.copy()
    title = lambda x: inflection.titleize(x)
    snakecase = lambda x: inflection.underscore(x)
    spaces = lambda x: x.replace(" ", "")
    cols_old = list(df.columns)
    cols_old = list(map(title, cols_old))
    cols_old = list(map(spaces, cols_old))
    cols_new = list(map(snakecase, cols_old))
    df.columns = cols_new
    return df

df1 = rename_columns(df1)

# Removendo valores "nan" da coluna 'cuisines'
df1 = df1.dropna(subset=['cuisines'])

# Função para trocar os códigos de país pelos seus nomes
COUNTRIES = {
    1: "India",
    14: "Australia",
    30: "Brazil",
    37: "Canada",
    94: "Indonesia",
    148: "New Zeland",
    162: "Philippines",
    166: "Qatar",
    184: "Singapure",
    189: "South Africa",
    191: "Sri Lanka",
    208: "Turkey",
    214: "United Arab Emirates",
    215: "England",
    216: "United States of America",
}
def country_name(country_id):
    return COUNTRIES[country_id]

# Comando para fazer o De-Para entre country_code e country_name
df1['country_code'] = df1['country_code'].apply(lambda x: country_name(x))

# Função para trocar os códigos de cores pelos seus nomes
COLORS = {
    "3F7E00": "darkgreen",
    "5BA829": "green",
    "9ACD32": "lightgreen",
    "CDD614": "orange",
    "FFBA00": "red",
    "CBCBC8": "darkred",
    "FF7800": "darkred",
}
def color_name(color_code):
    return COLORS[color_code]

# Comando para fazer o De-Para entre rating_color e color_name
df1['rating_color'] = df1['rating_color'].apply(lambda x: color_name(x))

# Selecionar apenas o primeiro tipo de culinária para cada restaurante
df1['cuisines'] = df1.loc[:, 'cuisines'].apply(lambda x: x.split(',')[0])

# Retirar duplicatas de restaurantes
df1_sem_restaurant_name_duplicada = df1.drop_duplicates(subset=['restaurant_name'])


#================================================
# Sidebar
#================================================

#Filtro de países
st.sidebar.markdown('## Filtros')
countries_list = df1['country_code'].unique()
country_options = st.sidebar.multiselect(
    'Escolha os Paises que Deseja visualizar as Informações',
    countries_list,
    default=['Brazil', 'England', 'Qatar', 'South Africa', 'Canada', 'Australia']
)
st.sidebar.markdown("""---""")
st.sidebar.markdown('Powered by Dev Leo Sales')

# Filtragem por países selecionados
linhas_selecionadas = df1['country_code'].isin(country_options)
df1 = df1.loc[linhas_selecionadas, :]
df1_sem_restaurant_name_duplicada = df1_sem_restaurant_name_duplicada.loc[linhas_selecionadas, :]

#================================================
# Layout no Streamlit
#================================================
st.markdown('# 🌎 Visão Países')

with st.container():
    #Quantidade de restaurantes registrados por país
    qtde_restaurantes_por_pais = (df1.loc[:, ['country_code', 'restaurant_id']]
                                  .groupby(['country_code'])
                                  .count()
                                  .sort_values(by='restaurant_id', ascending=False)
                                  .reset_index())
    fig = px.bar(qtde_restaurantes_por_pais,
                 x='country_code',
                 y='restaurant_id',
                 labels={   
                 'restaurant_id': 'Quantidade de restaurantes',
                 'country_code': 'País'
                 },
                 text_auto=True,
                )
    fig.update_traces(
        marker_color='rgb(198,205,220)'
    )
    fig.update_layout(
    title={
        'text': "Quantidade de restaurantes registrados por país",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        },
        plot_bgcolor='rgba(14,17,23, 0)'
        )
    # px.figure(facecolor='yellow')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    st.plotly_chart(fig, use_container_width=True)

with st.container():
    # Quantidade de cidades registrados por país
    # Remover duplicatas da coluna "city"
    df1_sem_city_duplicada = df1.drop_duplicates(subset=['city'])
    qtde_cidades_por_pais = (df1_sem_city_duplicada.loc[:, ['country_code', 'city']]
                                  .groupby(['country_code'])
                                  .count()
                                  .sort_values(by='city', ascending=False)
                                  .reset_index())
    fig = px.bar(qtde_cidades_por_pais,
                 x='country_code',
                 y='city',
                 labels={   
                 'city': 'Quantidade de cidades',
                 'country_code': 'País'
                 },
                 text_auto=True,
                 )
    fig.update_traces(
        marker_color='rgb(198,205,220)'
    )
    fig.update_layout(
    title={
        'text': "Quantidade de cidades registradas por país",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top',
        },
        plot_bgcolor='rgba(14,17,23, 0)'
        )
    # px.figure(facecolor='yellow')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False, showticklabels=False)
    st.plotly_chart(fig, use_container_width=True)

with st.container():
    col1, col2 = st.columns(2)

    with col1:
        media_avaliacoes_por_pais = (df1.loc[:, ['country_code', 'votes']]
                                     .groupby('country_code')
                                     .mean()
                                     .sort_values(by='votes', ascending=False)
                                     .reset_index())
        fig = px.bar(media_avaliacoes_por_pais,
                     x='country_code',
                     y='votes',
                     labels={   
                     'votes': 'Quantidade de votos',
                     'country_code': 'País'
                     },
                     text_auto=True,
                     )
        fig.update_traces(
        marker_color='rgb(198,205,220)'
        )
        fig.update_layout(
        title={
            'text': "Média de avaliações feitas por país",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            },
            plot_bgcolor='rgba(14,17,23, 0)'
            )
        # px.figure(facecolor='yellow')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False, showticklabels=False)
        col1.plotly_chart(fig, use_container_width=True)
    
    with col2:
        media_preco_prato_para_dois = (df1_sem_restaurant_name_duplicada.loc[:, ['country_code', 'average_cost_for_two']]
                                       .groupby('country_code')
                                       .mean('average_cost_for_two')
                                       .sort_values(by='average_cost_for_two', ascending=False)
                                       .reset_index())
        fig = px.bar(media_preco_prato_para_dois,
                     x='country_code',
                     y='average_cost_for_two',
                     labels={   
                     'average_cost_for_two': 'Preço de prato para 2 pessoas',
                     'country_code': 'País'
                     },
                     text_auto=True,
                     )
        fig.update_traces(
        marker_color='rgb(198,205,220)'
        )
        fig.update_layout(
        title={
            'text': "Média de preço de um prato de 2 pessoas por país",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            },
            plot_bgcolor='rgba(14,17,23, 0)'
            )
        # px.figure(facecolor='yellow')
        fig.update_xaxes(showgrid=False)
        fig.update_yaxes(showgrid=False, showticklabels=False)
        col2.plotly_chart(fig, use_container_width=True)