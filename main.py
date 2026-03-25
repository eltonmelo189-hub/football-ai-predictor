import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Carregamento dos Dados (Certifique-se que o caminho está correto)
try:
    data = pd.read_csv('data/football_data.csv')

    
    # 2. MENU LATERAL (Para evitar o erro de coluna inexistente)
    st.sidebar.header("Configurações da IA")
    if not data.empty:
        # Deixa o usuário escolher a coluna alvo ou define uma padrão
        coluna_alvo = st.sidebar.selectbox(
            "Coluna para Análise (Alvo):", 
            options=data.columns,
            index=0
        )
        
        # 3. FILTRO DE LIGA (Série A Brasil)
        liga_selecionada = st.sidebar.selectbox("Escolha a Liga:", ["Série A Brasil", "Premier League"])
        
        # Filtrar os dados baseados na escolha
        jogos_filtrados = data[data['liga'] == liga_selecionada]

        # 4. EXIBIÇÃO DOS JOGOS
        
        st.warning(f"Sem jogos de elite hoje para {liga_selecionada}. O filé mignon volta em breve!")


        if jogos_filtrados.empty:
            st.warning(f"Sem jogos de elite hoje para {liga_selecionada}. O filé mignon volta em breve!")
        else:
            st.write(jogos_filtrados) # Aqui mostra a tabela de jogos
            
            # 5. GRÁFICO DA IA (Onde estava o erro)
            st.subheader('Distribuição de Dados da IA')
            fig, ax = plt.subplots()
            sns.histplot(jogos_filtrados[coluna_alvo], kde=True, ax=ax)
            st.pyplot(fig)
st.error(f"Erro ao carregar dados: {e}")

except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
