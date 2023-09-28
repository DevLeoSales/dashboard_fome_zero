import streamlit as st
import pandas as pd
import inflection
import plotly.express as px

st.set_page_config(
    page_title="Cuisines",
    page_icon="🍽️",
    layout='wide'
)

# Leitura dos dados
df = pd.read_csv('dataset/zomato.csv')
df1 = df.copy()
df2 = df.copy()

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
df2 = rename_columns(df2)

# Removendo valores "nan" da coluna 'cuisines'
df1 = df1.dropna(subset=['cuisines'])
df2 = df2.dropna(subset=['cuisines'])

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
df2['country_code'] = df2['country_code'].apply(lambda x: country_name(x))

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
df2['rating_color'] = df2['rating_color'].apply(lambda x: color_name(x))

# Selecionar apenas o primeiro tipo de culinária para cada restaurante
df1['cuisines'] = df1.loc[:, 'cuisines'].apply(lambda x: x.split(',')[0])
df2['cuisines'] = df2.loc[:, 'cuisines'].apply(lambda x: x.split(',')[0])


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

#Filtro de quantidade de restaurantes
restaurant_slider = st.sidebar.slider(
    'Selecione a quantidade de Restaurantes/Culinárias que deseja visualizar', 
    value=10,
    min_value=0,
    max_value=20
)
st.sidebar.markdown("""---""")

#Filtro de culinarias
cuisines_list = df1['cuisines'].unique()
cuisines_options = st.sidebar.multiselect(
    'Escolha os Tipos de Culinária',
    cuisines_list,
    default=['Home-made', 'BBQ', 'Japanese', 'Brazilian', 'Arabian', 'American', 'Italian']
)
st.sidebar.markdown("""---""")
st.sidebar.markdown('Powered by Dev Leo Sales')

# Filtragem por países selecionados
linhas_selecionadas = df1['country_code'].isin(country_options)
df1 = df1.loc[linhas_selecionadas, :]

#Filtragem de quantidade de restaurantes
qtde_restaurantes = restaurant_slider

# Filtragem por culinarias selecionadas
linhas_selecionadas = df1['cuisines'].isin(cuisines_options)
df1 = df1.loc[linhas_selecionadas, :]

df1_sem_restaurant_name_duplicada = df1.drop_duplicates(subset=['restaurant_name'])

#================================================
# Layout no Streamlit
#================================================
st.markdown('# 🍽️ Visão Culinárias')

with st.container():
    st.markdown("## Melhores restaurantes dos principais tipos de culinária")
    col1, col2, col3, col4, col5 = st.columns(5)
    df2 = df2.drop_duplicates(subset=['restaurant_name'])


    with col1:
        #Comida italiana
        restaurantes_comida_italiana = df2[df2['cuisines'] == 'Italian']
        melhor_restaurante_italiana = (restaurantes_comida_italiana.loc[:, ['restaurant_name', 'aggregate_rating']]
                                       .groupby(['restaurant_name'])
                                       .mean()
                                       .sort_values(by='aggregate_rating', ascending=False)
                                       .reset_index()).head(1).iloc[0, 0]
        melhor_restaurante_italiana_nota = (restaurantes_comida_italiana.loc[:, ['restaurant_name', 'aggregate_rating']]
                                       .groupby(['restaurant_name'])
                                       .mean()
                                       .sort_values(by='aggregate_rating', ascending=False)
                                       .reset_index()).head(1).iloc[0, 1]
        col1.metric('Italiana: ' + str(melhor_restaurante_italiana), str(melhor_restaurante_italiana_nota) + '/5.0')

    with col2:
        #Comida americana
        restaurantes_comida_americana = df2[df2['cuisines'] == 'American']
        melhor_restaurante_americana = (restaurantes_comida_americana.loc[:, ['restaurant_name', 'aggregate_rating']]
                                       .groupby(['restaurant_name'])
                                       .mean()
                                       .sort_values(by='aggregate_rating', ascending=False)
                                       .reset_index()).head(1).iloc[0, 0]
        melhor_restaurante_americana_nota = (restaurantes_comida_americana.loc[:, ['restaurant_name', 'aggregate_rating']]
                                       .groupby(['restaurant_name'])
                                       .mean()
                                       .sort_values(by='aggregate_rating', ascending=False)
                                       .reset_index()).head(1).iloc[0, 1]
        col2.metric('Americana: ' + str(melhor_restaurante_americana), str(melhor_restaurante_americana_nota) + '/5.0')

    with col3:
        #Comida japanese
        restaurantes_comida_arabian = df2[df2['cuisines'] == 'Arabian']
        melhor_restaurante_arabian = (restaurantes_comida_arabian.loc[:, ['restaurant_name', 'aggregate_rating']]
                                       .groupby(['restaurant_name'])
                                       .mean()
                                       .sort_values(by='aggregate_rating', ascending=False)
                                       .reset_index()).head(1).iloc[0, 0]
        melhor_restaurante_arabian_nota = (restaurantes_comida_arabian.loc[:, ['restaurant_name', 'aggregate_rating']]
                                       .groupby(['restaurant_name'])
                                       .mean()
                                       .sort_values(by='aggregate_rating', ascending=False)
                                       .reset_index()).head(1).iloc[0, 1]
        col3.metric('Arabian: ' + str(melhor_restaurante_arabian), str(melhor_restaurante_arabian_nota) + '/5.0')

    with col4:
        #Comida japanese
        restaurantes_comida_japanese = df2[df2['cuisines'] == 'Japanese']
        melhor_restaurante_japanese = (restaurantes_comida_japanese.loc[:, ['restaurant_name', 'aggregate_rating']]
                                       .groupby(['restaurant_name'])
                                       .mean()
                                       .sort_values(by='aggregate_rating', ascending=False)
                                       .reset_index()).head(1).iloc[0, 0]
        melhor_restaurante_japanese_nota = (restaurantes_comida_japanese.loc[:, ['restaurant_name', 'aggregate_rating']]
                                       .groupby(['restaurant_name'])
                                       .mean()
                                       .sort_values(by='aggregate_rating', ascending=False)
                                       .reset_index()).head(1).iloc[0, 1]
        col4.metric('Japanese: ' + str(melhor_restaurante_japanese), str(melhor_restaurante_japanese_nota) + '/5.0')

    with col5:
        #Comida brazilian
        restaurantes_comida_brazilian = df2[df2['cuisines'] == 'Brazilian']
        melhor_restaurante_brazilian = (restaurantes_comida_brazilian.loc[:, ['restaurant_name', 'aggregate_rating']]
                                       .groupby(['restaurant_name'])
                                       .mean()
                                       .sort_values(by='aggregate_rating', ascending=False)
                                       .reset_index()).head(1).iloc[0, 0]
        melhor_restaurante_brazilian_nota = (restaurantes_comida_brazilian.loc[:, ['restaurant_name', 'aggregate_rating']]
                                       .groupby(['restaurant_name'])
                                       .mean()
                                       .sort_values(by='aggregate_rating', ascending=False)
                                       .reset_index()).head(1).iloc[0, 1]
        col5.metric('Brasileira: ' + str(melhor_restaurante_brazilian), str(melhor_restaurante_brazilian_nota) + '/5.0')

with st.container():
    st.markdown('## Top ' + str(qtde_restaurantes) + ' restaurantes')

    melhores_restaurantes = (df1_sem_restaurant_name_duplicada.loc[:, ['restaurant_id', 'restaurant_name', 'country_code', 'city', 'cuisines', 'average_cost_for_two', 'votes', 'aggregate_rating']]
                                    .groupby(['restaurant_id', 'restaurant_name', 'country_code', 'city', 'cuisines', 'average_cost_for_two', 'votes'])
                                    .mean('aggregate_rating')
                                    .sort_values(by='votes', ascending=False)
                                    .reset_index())
    top_10_melhores_restaurantes = (melhores_restaurantes[melhores_restaurantes['aggregate_rating'] == melhores_restaurantes['aggregate_rating'].max()]
                                    .sort_values(by='votes', ascending=False)
                                    .head(qtde_restaurantes))
    st.dataframe(top_10_melhores_restaurantes)

with st.container():
    col1, col2 = st.columns(2, gap="large")

    with col1:
        # Top melhores culinárias
        top_10_culinarias = (df2.loc[:, ['cuisines', 'aggregate_rating']]
                                    .groupby(['cuisines'])
                                    .mean()
                                    .sort_values(by='aggregate_rating', ascending=False)
                                    .reset_index()).head(qtde_restaurantes)
        fig = px.bar(top_10_culinarias,
                     x='cuisines',
                     y='aggregate_rating',
                     labels={   
                     'cuisines': 'Culinária',
                     'aggregate_rating': 'Média de avaliação'
                     },
                     text_auto=True,
                     )
        fig.update_traces(
        marker_color='rgb(198,205,220)'
        )
        fig.update_layout(
        title={
            'text': "Top " + str(qtde_restaurantes) + " culinárias melhores avaliadas",
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
        col1.plotly_chart(fig)
    
    with col2:
        # bot melhores culinárias
        bot_10_culinarias = (df2.loc[:, ['cuisines', 'aggregate_rating']]
                                    .groupby(['cuisines'])
                                    .mean()
                                    .sort_values(by='aggregate_rating')
                                    .reset_index()).head(qtde_restaurantes)
        fig = px.bar(bot_10_culinarias,
                     x='cuisines',
                     y='aggregate_rating',
                     labels={   
                     'cuisines': 'Culinária',
                     'aggregate_rating': 'Média de avaliação'
                     },
                     text_auto=True,
                     )
        fig.update_traces(
        marker_color='rgb(198,205,220)'
        )
        fig.update_layout(
        title={
            'text': str(qtde_restaurantes) +" culinárias piores avaliadas",
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
        col2.plotly_chart(fig)