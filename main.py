import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregamento dos Dados
try:
    data = pd.read_csv('data/football_data.csv')
    
    # 2. MENU LATERAL
    st.sidebar.header("Configurações da IA")
    if not data.empty:
        coluna_alvo = st.sidebar.selectbox(
            "Coluna para Análise (Alvo):", 
            options=data.columns,
            index=0
        )
        
        # 3. FILTRO DE LIGA
        liga_selecionada = st.sidebar.selectbox("Escolha a Liga:", ["Série A Brasil", "Premier League"])
        
        # Filtrar os dados
        jogos_filtrados = data[data['liga'] == liga_selecionada]

        # 4. EXIBIÇÃO DOS JOGOS
        st.title(f"⚽ Predator: {liga_selecionada}")
        
        if jogos_filtrados.empty:
            st.warning(f"Sem jogos de elite hoje para {liga_selecionada}. O filé mignon volta em breve!")
        else:
            st.write(jogos_filtrados) 
            
            # 5. GRÁFICO DA IA
            st.subheader('Distribuição de Dados da IA')
            fig, ax = plt.subplots()
            sns.histplot(jogos_filtrados[coluna_alvo], kde=True, ax=ax)
            st.pyplot(fig)

except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
