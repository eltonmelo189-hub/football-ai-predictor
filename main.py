import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Predator - Palpites", layout="wide")

try:
    df = pd.read_csv('data/football_data.csv')
    st.title("⚽ predator: palpite automático")
    
    # Lógica do Palpite (O robô analisa os gols)
    def calcular_palpite(row):
        if row['home_score'] > row['away_score'] + 0.5:
            return "✅ Casa Vence"
        elif row['away_score'] > row['home_score'] + 0.5:
            return "🚀 Fora Vence"
        else:
            return "🤝 Empate / Ambas"

    # Cria a coluna de palpite na hora
    df['PALPITE'] = df.apply(calcular_palpite, axis=1)

    # Mostra a tabela com tudo: Data, Hora, Times e o Palpite do Robô
    st.subheader("lista de jogos e dicas de hoje")
    st.dataframe(df[['data', 'hora', 'casa', 'fora', 'PALPITE', 'liga']])

    # Gráfico de tendência
    st.divider()
    st.subheader("📈 análise de força (gols)")
    fig, ax = plt.subplots()
    sns.barplot(data=df, x='casa', y='home_score', ax=ax, palette="Blues")
    plt.xticks(rotation=45)
    st.pyplot(fig)

except Exception as e:
    st.error(f"erro: {e}")
