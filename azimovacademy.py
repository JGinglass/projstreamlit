import streamlit as st
import pandas as pd

# Altera o layout padrão da página
st.set_page_config(layout="wide", page_title="Teste Curso Azimov")

# Carrega os dados do arquivo para o dataframe
df = pd.read_csv("/home/jpginglass/Documentos/projetosvscode/azimovstream/spotify.csv")

# Troca o indice para que seja o valor da coluna Track
df.set_index("Track", inplace=True)

# Cria uma lista com o nome único de artistas (sem repetição) e ordenada
# o value_count gera uma Serie (tipo do pandas) com o indice e quantas vezes aparece
# assim essa Serie só tem os artistas no indicce sem duplicação de nomes. 
artistas = df["Artist"].value_counts().sort_index().index

# Relaciona a seleção do artista na página e atribui a variavel artista_seleconado
artista_selecionado = st.selectbox("Selecione o artista", artistas)

# cria um novo dataframe com o resultado do filtro pelo artista selecionado na pagina
df_2 = df[df["Artist"]==artista_selecionado]

# para gerar um dataframe com a selecao de apenas duas colunas 
# com pandas ordenado pelo valor da coluna Stream: 
df.loc[:,["Stream","Comments"]].sort_values(by="Stream")

#Cria um grafico de barra com os streams de cada Track do artista selecionado
st.bar_chart(df_2["Stream"])

# Inclui um texto na pagina usando formatação markdown
st.markdown(f"## _Comentários_ e _Likes_ do *{artista_selecionado}*")

# Inclui um novo grafico de comentários e likes por Track
st.bar_chart(stack=False,horizontal=True,data=df_2.loc[:,["Comments","Likes"]])
