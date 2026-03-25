import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    # Carregar dados
    data = pd.read_csv('data/football_data.csv')
    st.sidebar.header("Menu")
    
    if not data.empty:
        col = st.sidebar.selectbox("Análise:", options=data.columns)
        liga = st.sidebar.selectbox("Liga:", ["Série A Brasil", "Premier League"])
        
        # Filtro
        if 'liga' in data.columns:
            df = data[data['liga'] == liga]
        else:
            df = pd.DataFrame()

        st.title(f"⚽ Predator: {liga}")
        
        if df.empty:
            st.warning("Sem jogos para esta liga no momento.")
        else:
            st.write(df)
            # Gráfico
            fig, ax = plt.subplots()
            sns.histplot(data=df, x=col, kde=True, ax=ax)
            st.pyplot(fig)
except Exception as e:
    st.error(f"Erro: {e}")
