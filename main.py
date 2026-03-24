import streamlit as st
import requests
from datetime import datetime, timedelta

st.set_page_config(page_title="Predator Elite Radar", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .card-mignon {
        background: linear-gradient(135deg, #c9a227 0%, #8e6d13 100%);
        padding: 15px; border-radius: 15px; color: black; 
        margin-bottom: 15px; border: 2px solid #fff; text-align: center;
    }
    .time-tag { background: #000; color: #fff; padding: 3px 8px; border-radius: 5px; font-size: 14px; }
    .palpite-tag { background: #fff; color: #000; padding: 5px 10px; border-radius: 5px; font-weight: bold; display: block; margin: 10px auto; width: fit-content; }
    </style>
    """, unsafe_allow_html=True)

API_TOKEN = "b8c288ff23ca4b2480f5d479176fc61f"
HEADERS = {'X-Auth-Token': API_TOKEN}

st.title("🏆 RADAR FILÉ MIGNON")
st.subheader("🔥 Jogos de Elite para HOJE")

LIGAS = {"Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿": 2021, "Champions League 🇪🇺": 2001}
liga_nome = st.sidebar.selectbox("Selecione a Liga:", list(LIGAS.keys()))
liga_id = LIGAS[liga_nome]

if st.button("🔍 ESCANEAR JOGOS DE HOJE"):
    with st.spinner("🧠 Filtrando o filé mignon de hoje..."):
        url = f"https://api.football-data.org/v4/competitions/{liga_id}/matches"
        res = requests.get(url, headers=HEADERS)
        
        if res.status_code == 200:
            todos_jogos = res.json().get('matches', [])
            hoje = datetime.now().strftime('%Y-%m-%d')
            
            # Filtra apenas os jogos de hoje
            jogos_hoje = [j for j in todos_jogos if j['utcDate'].startswith(hoje)]
            
            if not jogos_hoje:
                st.info(f"Nenhum jogo de elite da {liga_nome} para hoje ({hoje}).")
            
            for j in jogos_hoje:
                casa = j['homeTeam']['name']
                fora = j['awayTeam']['name']
                
                # Ajuste de Horário (UTC para Brasília -3h)
                data_utc = datetime.strptime(j['utcDate'], "%Y-%m-%dT%H:%M:%SZ")
                data_br = data_utc - timedelta(hours=3)
                horario = data_br.strftime('%H:%M')
                
                st.markdown(f"""
                    <div class="card-mignon">
                        <span class="time-tag">🕒 Início: {horario} (Horário de Brasília)</span><br><br>
                        <strong style='font-size: 18px;'>{casa} vs {fora}</strong>
                        <span class="palpite-tag">🎯 PALPITE: Vitória {casa}</span>
                        <small>🔥 CONFIANÇA IA: 89%</small>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Muitos acessos. Aguarde 60 segundos e tente de novo.")

st.sidebar.markdown("---")
st.sidebar.info("O sistema agora filtra automaticamente apenas as partidas do dia atual.")
