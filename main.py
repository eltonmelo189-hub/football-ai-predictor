import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    data = pd.read_csv('data/football_data.csv')
    st.sidebar.header("Configurações")
    
    if not data.empty:
        coluna = st.sidebar.selectbox("Análise:", options=data.columns)
        liga = st.sidebar.selectbox("Liga:", ["Série A Brasil", "Premier League"])
        
        if 'liga' in data.columns:
            df = data[data['liga'] == liga]
        else:
            df = pd.DataFrame()

        st.title(f"⚽ Predator: {liga}")
        
        if df.empty:
            st.warning("Sem jogos para esta liga no momento.")
        else:
            st.write(df)
            fig, ax = plt.subplots()
            sns.histplot(data=df, x=coluna, kde=True, ax=ax)
            st.pyplot(fig)
except Exception as e:
    st.error(f"Erro: {e}")
