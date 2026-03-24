import streamlit as st
import requests
from datetime import datetime, timedelta

st.set_page_config(page_title="Predator Teste Geral", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .card-teste {
        background: #1a1c23; padding: 15px; border-radius: 10px; 
        border: 1px solid #c9a227; margin-bottom: 10px;
    }
    .badge { background: #c9a227; color: black; padding: 2px 8px; border-radius: 5px; font-size: 12px; }
    </style>
    """, unsafe_allow_html=True)

API_TOKEN = "b8c288ff23ca4b2480f5d479176fc61f"
HEADERS = {'X-Auth-Token': API_TOKEN}

st.title("📡 SCANNER DE TESTE GERAL")
st.write("Buscando qualquer jogo disponível no mundo agora...")

if st.button("🚀 FORÇAR BUSCA COMPLETA"):
    # Esta URL busca TODOS os jogos do dia, de qualquer liga
    url = "https://api.football-data.org/v4/matches"
    
    try:
        res = requests.get(url, headers=HEADERS)
        if res.status_code == 200:
            dados = res.json()
            jogos = dados.get('matches', [])
            
            if not jogos:
                st.info("Realmente não há jogos registrados para agora na base de dados.")
            else:
                st.success(f"Encontrei {len(jogos)} jogos rolando ou agendados!")
                for j in jogos[:15]: # Mostra os primeiros 15 para testar
                    liga = j['competition']['name']
                    casa = j['homeTeam']['name']
                    fora = j['awayTeam']['name']
                    
                    st.markdown(f"""
                        <div class="card-teste">
                            <span class="badge">{liga}</span><br>
                            <strong>{casa} vs {fora}</strong>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.error(f"Erro na API: {res.status_code}. Pode ser o limite de acessos do plano grátis.")
    except:
        st.error("Erro de conexão. Verifique o link do Streamlit.")

st.sidebar.warning("⚠️ MODO DE TESTE: Este código ignora o filtro de 'Filé Mignon' para testar a sua chave.")
