import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    # Carrega os dados
    dados = pd.read_csv('data/football_data.csv')
    st.sidebar.header("Menu")
    
    if not dados.empty:
        # Cria o seletor de colunas com o que existir na planilha
        col = st.sidebar.selectbox("Analise:", options=dados.columns)
        
        # Tenta filtrar pela liga apenas se a coluna existir
        if 'liga' in dados.columns:
            lista_ligas = dados['liga'].unique().tolist()
            L = st.sidebar.selectbox("Liga:", options=lista_ligas)
            df = dados[dados['liga'] == L]
        else:
            # Se não tiver a coluna 'liga', mostra tudo o que tem na planilha
            st.sidebar.warning("Coluna 'liga' não encontrada. Mostrando todos os dados.")
            df = dados
            L = "Todos os Jogos"

        st.title(f"⚽ Predator: {L}")
        
        if df.empty:
            st.warning("Sem jogos encontrados.")
        else:
            st.write(df) # Aqui vai aparecer a tabela com data, hora e times
            fig, ax = plt.subplots()
            sns.histplot(data=df, x=col, kde=True, ax=ax)
            st.pyplot(fig)
            
except Exception as e:
    st.error(f"Erro: {e}")
