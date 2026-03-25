import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('data/football_data.csv')
    st.title("predator v2")
    
    if 'liga' in df.columns:
        ligas = df['liga'].unique().tolist()
        escolha = st.sidebar.selectbox("liga:", ["todas"] + ligas)
        if escolha != "todas":
            df = df[df['liga'] == escolha]

    st.subheader("jogos")
    st.write(df)

    fig, ax = plt.subplots()
    sns.histplot(data=df, x="home_score", kde=True, ax=ax)
    st.pyplot(fig)

except Exception as e:
    st.error(f"erro: {e}")
