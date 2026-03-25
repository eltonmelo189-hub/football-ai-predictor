import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

try:
    df_all = pd.read_csv('data/football_data.csv')
    st.sidebar.header("Menu")
    
    if not df_all.empty:
        c = st.sidebar.selectbox("Coluna:", options=df_all.columns)
        L = st.sidebar.selectbox("Liga:", ["Série A Brasil", "Premier League"])
        
        df = df_all[df_all['liga'] == L]
        
        st.title(f"⚽ Predator: {L}")
        
        if df.empty:
            st.warning("Sem jogos.")
        else:
            st.write(df)
            fig, ax = plt.subplots()
            sns.histplot(data=df, x=c, kde=True, ax=ax)
            st.pyplot(fig)
except Exception as e:
    st.error(f"Erro: {e}")
