# 1. Problema de negócio
Você acaba de ser contratado como Cientista de Dados da empresa Fome Zero, e a sua principal tarefa nesse momento é ajudar o CEO Kleiton Guerra a identificar pontos chaves da empresa, respondendo às perguntas que ele fizer utilizando dados!
A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core business é facilitar o encontro e negociações de clientes e restaurantes. Os restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza informações como endereço, tipo de culinária servida, se possui reservas, se faz entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações. Para isso, foram realizados as seguintes análises:
  ## 1. Visão Geral:
    1. Quantos restaurantes únicos estão registrados?
    2. Quantos países únicos estão registrados?
    3. Quantas cidades únicas estão registradas?
    4. Qual o total de avaliações feitas?
    5. Qual o total de tipos de culinária registrados? 
  ## 2. Visão por País:
    1. Qual o nome do país que possui mais cidades registradas?
    2. Qual o nome do país que possui mais restaurantes registrados?
    3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4
    registrados?
    4. Qual o nome do país que possui a maior quantidade de tipos de culinária
    distintos?
    5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
    6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem
    entrega?
    7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam
    reservas?
    8. Qual o nome do país que possui, na média, a maior quantidade de avaliações
    registrada?
    9. Qual o nome do país que possui, na média, a maior nota média registrada?
    10. Qual o nome do país que possui, na média, a menor nota média registrada?
    11. Qual a média de preço de um prato para dois por país?
  ## 3. Visão por Cidade:
    1. Qual o nome da cidade que possui mais restaurantes registrados?
    2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
    3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
    4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
    5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
    6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
    7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
    8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?
  ## 4. Visão Restaurante
    1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
    2. Qual o nome do restaurante com a maior nota média?
    3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
    4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
    5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
    6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
    7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
    8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?
  ## 5. Visão por Tipos de Culinária
    1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
    2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
    3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
    4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
    5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
    6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
    7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
    8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
    9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
    10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
    11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
    12. Qual o tipo de culinária que possui a maior nota média?
    13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?

# 2. Premissas para análise
  1. Para os principais tipos de culinária, foram considerados Italiana, Americana, Árabe, Japonesa e Brasileira
  2. Nas análises de restaurantes, caso houvesse algum empate, o critério de desempate foi o tempo que o restaurante está cadastrado na plataforma, sendo considerado o mais antigo
  3. As 4 principais visões de negócio, utilizadas para gerar os dashboards, foram:
    1. Visão Geral
    2. Visão por País
    3. Visão Por Tipo de Culinária
    4. Visão por Cidade
# 3. Estratégia da solução
Para cada uma das visões, foram geradas as seguintes visualizações:
  1. Visão Geral:
    1. Quantidade de restaurantes cadastrados
    2. Quantidade de Países cadastrados
    3. Quantidade de Cidades cadastrada
    4. Quantidade de avaliações feitas
    5. Quantidade de tipos de culinária diferentes
    6. Mapa com a localização de todos os restaurantes cadastrados na plataforma
    7. Filtro para poder limitar quais países deseja ver informações
  2. Visão por País:
    1. Melhores restaurantes para os principais tipos de culinária
    2. Top restaurantes com melhor avaliação
    3. Top Culinárias com melhor avaliação
    4. Tipos de culinárias piores avaliadas
    5. Filtro para poder limitar quais países deseja ver informações
    6. Filtro para poder limitar a quantidade de informações que deseja visualizar
    7. Filtro para poder limitar quais tipos de culinária deseja ver
  3. Visão por Tipo de Culinária:
    1. Quantidade de restaurantes cadastrados
    2. Quantidade de Cidades cadastrada
    3. Quantidade de avaliações feitas
    4. Preço médio de um prato para 2 pessoas
    5. Filtro para poder limitar quais países deseja ver informações
  4. Visão por Cidade:
    1. Top cidades com mais restaurantes cadastrados
    2. Top cidades com mais restaurantes com avaliação média maior que 4
    3. Cidades com mais restaurantes com avaliação média menor que 2.5
    4. Top cidades com mais tipos culinários diferentes
    5. Filtro para poder limitar quais países deseja ver informações

# 4. Top 3 Insights de dados
# 5. O produto final do projeto
# 6. Conclusão
O objetivo desse projeto é criar um conjunto de gráficos e/ou tabelas
que exibam essas métricas da melhor forma possível para o CEO.
Da visão da Empresa, podemos concluir que o número de pedidos
cresceu entre a semana 06 e a semana 13 do ano de 2022.
# 7. Próximo passos
  1. Reduzir o número de métricas.
  2. 2. Criar novos filtros.
  3. Adicionar novas visões de negócio.
