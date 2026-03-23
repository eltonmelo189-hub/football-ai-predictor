import sys
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns

# Função de coleta de dados
def collect_data():
    data = pd.read_csv('data/football_data.csv')
    return data

# Função de exploração
def explore_data(data):
    st.write(data.describe())
    st.subheader('Data Distribution')
    sns.histplot(data['target_column'])
    st.pyplot()
    plt.figure(figsize=(10, 6))
    sns.heatmap(data.corr(), annot=True)
    st.pyplot()

# Função de treino
def train_model(data):
    X = data.drop('target_column', axis=1)
    y = data['target_column']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    return model, accuracy

# App Principal
def main():
    st.title('Football AI Predictor')
    
    # CHAVE CORRIGIDA AQUI:
    api_key = "b8c288ff23ca4b2480f5d479176cf61f"
    league_id = "71"
    
    data = collect_data()
    explore_data(data)
    model, accuracy = train_model(data)
    st.write('Model Accuracy:', accuracy)
    
    if api_key != "":
        st.success("API configurada com sucesso! Carregando jogos do Brasileirão...")

if __name__ == '__main__':
    main()
