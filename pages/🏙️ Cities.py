import streamlit as st
import pandas as pd
import inflection
import plotly.express as px

st.set_page_config(
    page_title="Home",
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
st.markdown('# 🏙️ Visão Cidades')
with st.container():
    #Top 10 cidades com mais restaurantes
    top_10_cidades_mais_restaurantes = (df1.loc[:, ['city', 'country_code', 'restaurant_id']]
                                  .groupby(['city', 'country_code'])
                                  .count()
                                  .sort_values(by='restaurant_id', ascending=False)
                                  .reset_index())
    fig = px.bar(top_10_cidades_mais_restaurantes.head(10),
                 x='city',
                 y='restaurant_id',
                     labels={   
                     'city': 'Cidades',
                     'restaurant_id': 'Quantidade de restaurantes',
                     'country_code': 'País'
                     },
                     text_auto=True,
                     color='country_code'
                     )
    fig.update_layout(
    title={
        'text': "Top 10 cidades com mais restaurantes",
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
    col1, col2 = st.columns(2, gap="large")

    with col1:
        #top 7 cidades com média de avaliação maior que 4
        restaurantes_media_maior_que_4 = df1[df1['aggregate_rating'] > 4]
        cidades_restaurantes_nota_maior_4 = (restaurantes_media_maior_que_4.loc[:, ['city', 'country_code', 'restaurant_id']]
                                  .groupby(['city', 'country_code'])
                                  .count()
                                  .sort_values(by='restaurant_id', ascending=False)
                                  .reset_index())
        fig = px.bar(cidades_restaurantes_nota_maior_4.head(7),
                     x='city',
                     y='restaurant_id',
                     labels={   
                     'city': 'Cidades',
                     'restaurant_id': 'Quantidade de restaurantes',
                     'country_code': 'País'
                     },
                     text_auto=True,
                     color='country_code'
                     )
        fig.update_layout(
        title={
            'text': "Top 7 cidades com restaurantes com avaliação média maior que 4",
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
        #top 7 cidades com média de avaliação menor que 2.5
        restaurantes_media_menor_2_5 = df1[df1['aggregate_rating'] < 2.5]
        cidades_restaurantes_nota_menor_2_5 = (restaurantes_media_menor_2_5.loc[:, ['city', 'country_code', 'restaurant_id']]
                                  .groupby(['city', 'country_code'])
                                  .count()
                                  .sort_values(by='restaurant_id', ascending=False)
                                  .reset_index())
        fig = px.bar(cidades_restaurantes_nota_menor_2_5.head(7),
                     x='city',
                     y='restaurant_id',
                     labels={   
                     'city': 'Cidades',
                     'restaurant_id': 'Quantidade de restaurantes',
                     'country_code': 'País'
                     },
                     text_auto=True,
                     color='country_code'
                     )
        fig.update_layout(
        title={
            'text': "Top 7 cidades com restaurantes com avaliação média menos que 2.5",
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

with st.container():
    # Top 10 cidades com mais restaurantes com tipos culinários distintos
    df2 = df1_sem_restaurant_name_duplicada.copy()
    df2['aux'] = df2['city'] + df2['cuisines']
    df2 = df2.drop_duplicates(subset=['aux'])
    cidades_mais_culinarias_distintas = (df2.loc[:, ['city', 'country_code', 'restaurant_id']]
                                         .groupby(['city', 'country_code'])
                                         .count()
                                         .sort_values(by='restaurant_id', ascending=False)
                                         .reset_index())
    fig = px.bar(cidades_mais_culinarias_distintas.head(10),
                 x='city',
                 y='restaurant_id',
                     labels={   
                     'city': 'Cidades',
                     'restaurant_id': 'Quantidade de restaurantes',
                     'country_code': 'País'
                     },
                     text_auto=True,
                     color='country_code'
                     )
    fig.update_layout(
    title={
        'text': "Top 10 cidades com mais restaurantes com tipos culinários distintos",
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