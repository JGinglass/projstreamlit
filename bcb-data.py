import streamlit as st
import pandas as pd

# Altera o layout padrão da página
st.set_page_config(layout="wide", page_title="Teste Curso Azimov")

# Carrega os dados do arquivo para o dataframe
df = pd.read_csv("~/Documentos/projetosvscode/projstreamtest/dados_bcb.csv", sep=";", date_format="%d/%m/%Y", parse_dates=["data"])
df.set_index(inplace=True,keys="data")

# Troca vírgula por ponto na coluna "valor"
df["valor"] = df["valor"].str.replace(",", ".")

# Define o tipo da coluna "valor" como numérico
df["valor"] = pd.to_numeric(df["valor"], errors='coerce')

df_filtrado = df.loc["01/01/2019":"01/01/2025"]
st.line_chart(df_filtrado["valor"])
df_filtrado 
