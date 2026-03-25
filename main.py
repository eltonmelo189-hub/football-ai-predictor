import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    dados = pd.read_csv('data/football_data.csv')
    st.sidebar.header("Menu")
    if not dados.empty:
      c = st.sidebar.selectbox("Analise:", options=dados.columns)
      L = st.sidebar.selectbox("Liga:", ["Série A Brasil", "Premier League"])
       df = dados[dados['liga'] == L] if 'liga' in dados.columns else dados
      st.title(f"Predator: {L}")
       if df.empty:
           st.warning("Sem jogos.")
      else:
           st.write(df)
          fig, ax = plt.subplots()
           l sns.histplot(data=df, x=c, kde=True, ax=ax)
           st.pyplot(fig)
except Exception as e:
  st.error(f"Erro: {e}")
