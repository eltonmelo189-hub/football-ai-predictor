import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Predator V2", layout="wide")

try:
    df = pd.read_csv('data/football_data.csv')
    st.sidebar.header("Painel de Controle")
    
    if 'liga' in df.columns:
        ligas = df['liga'].unique().tolist()
        escolha = st.sidebar.selectbox("Escolha a Liga:", ["Todas"] + ligas)
        if escolha != "Todas":
            df = df[df['liga'] == escolha]
            st.title(f"Predator: {escolha}")
        else:
            st.title("Predator: Todos os Jogos")
    else:
        st.title("Predator: Geral")

    st.subheader("Lista de Confrontos")
    st.write(df)

    st.divider()
    st.subheader("Analise de Gols")
    col_analise = st.sidebar.selectbox("Ver grafico de:", ["home_score", "away_score"])
    
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.histplot(data=df, x=col_analise, kde=True, color="skyblue", ax=ax)
    st.pyplot(fig)

except Exception as e:
    st.error(f"Erro: {e}")
