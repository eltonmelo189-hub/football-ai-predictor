import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Configuração da página para o celular
st.set_page_config(page_title="Predator V2", layout="wide")

try:
    # 1. Carregar os dados que você acabou de salvar
    df = pd.read_csv('data/football_data.csv')
    
    st.sidebar.header("📊 Painel de Controle")
    
    # 2. Filtro de Liga (Vai funcionar agora que a coluna existe!)
    if 'liga' in df.columns:
        ligas = df['liga'].unique().tolist()
        escolha = st.sidebar.selectbox("Escolha a Liga:", ["Todas"] + ligas)
        if escolha != "Todas":
            df = df[df['liga'] == escolha]
            st.title(f"⚽ Predator: {escolha}")
        else:
            st.title("⚽ Predator: Todos os Jogos")
    else:
        st.title("⚽ Predator: Geral")

    # 3. Mostrar a Tabela com Times, Data e Hora
    st.subheader("Lista de Confrontos")
    st.write(df)

    # 4. Análise Gráfica
    st.divider()
    st.subheader("📈 Análise de Gols")
    # Deixa escolher qual coluna analisar no gráfico
    col_analise = st.sidebar.selectbox("Ver gráfico de:", ["home_score", "away_score"])
    
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.histplot(data=df, x=col_analise, kde=True, color="skyblue", ax=ax)
    st.pyplot(fig)

except Exception as e:
    st.error(f"Erro ao carregar o Predator: {e}")
