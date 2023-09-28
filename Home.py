import streamlit as st
import pandas as pd
import inflection
import folium
from streamlit_folium import folium_static
from folium.plugins import MarkerCluster

st.set_page_config(
    page_title="Main Page",
    page_icon="📊",
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

# Retirar duplicatas de restaurantes
df1_sem_restaurant_name_duplicada = df1.drop_duplicates(subset=['restaurant_name'])
df2_sem_restaurant_name_duplicada = df2.drop_duplicates(subset=['restaurant_name'])

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
st.markdown('# Fome Zero!')
st.markdown('## O melhor lugar para encontrar seu mais novo restaurante favorito')
st.markdown('### Temos as seguintes marcas dentro da nossa plataforma:')

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        #Quantidade de restaurantes cadastrados
        restaurantes_unicos = df2['restaurant_name'].nunique()
        col1.metric('Restaurantes cadastrados', restaurantes_unicos)
    
    with col2:
        #Quantidade de países cadastrados
        paises_unicos = df2['country_code'].nunique()
        col2.metric('Países cadastrados', paises_unicos)
    
    with col3:
        #Quantidade de cidades cadastrados
        cidades_unicos = df2['city'].nunique()
        col3.metric('Cidades cadastrados', cidades_unicos)

    with col4:
        #Quantidade de avaliações feitas
        quantidade_de_avaliacoes = df2_sem_restaurant_name_duplicada['votes'].sum()
        col4.metric('Quantidade de avaliações', quantidade_de_avaliacoes)
    
    with col5:
        # Calcular a quantidade valores únicos da coluna "cuisines"
        culinarias_unicas = df2['cuisines'].nunique()
        col5.metric('Quantidade de culinárias', culinarias_unicas)

with st.container():
    df_aux_6 = df1_sem_restaurant_name_duplicada.loc[:, ['restaurant_id', 'restaurant_name', 'cuisines', 'average_cost_for_two', 'aggregate_rating', 'latitude', 'longitude', 'rating_color', 'currency', 'country_code']].groupby(['restaurant_id', 'restaurant_name', 'cuisines', 'average_cost_for_two', 'aggregate_rating', 'rating_color', 'currency', 'country_code']).median().reset_index()
    
    map = folium.Map(zoom_start=2)

    marker_cluster = MarkerCluster().add_to(map)

    
    
    for index, location_info in df_aux_6.iterrows():
        folium.Marker([location_info['latitude'],
                        location_info['longitude']],
                        icon=folium.Icon(color=df_aux_6.loc[index, 'rating_color'], icon='home'),
                        popup=folium.Popup(f"<strong>{location_info['restaurant_name']}</strong></br></br> Price: {location_info['average_cost_for_two']:.2f} {location_info['currency']} para dois</br> Type: {location_info['cuisines']}</br> Country: {location_info['country_code']}</br> Rating: {location_info['aggregate_rating']}/5.0", max_width=500)).add_to(marker_cluster)
        
    folium_static(map, width=1024, height=600)