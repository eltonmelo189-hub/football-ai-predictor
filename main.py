import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    dados = pd.read_csv('data/football_data.csv')
    st.sidebar.header("Menu")
    
    if not dados.empty:
        col = st.sidebar.selectbox("Analise:", options=dados.columns)
        liga = st.sidebar.selectbox("Liga:", ["Série A Brasil", "Premier League"])
        
        # Filtro simples
        if 'liga' in dados.columns:
            df = dados[dados['liga'] == liga]
        else:
            df = dados

        st.title(f"⚽ Predator: {liga}")
        
        if df.empty:
            st.warning("Sem jogos para esta liga.")
        else:
            st.write(df)
            fig, ax = plt.subplots()
            sns.histplot(data=df, x=col, kde=True, ax=ax)
            st.pyplot(fig)
            
except Exception as e:
    st.error(f"Erro: {e}")
