import streamlit as st
import requests
from datetime import datetime, timedelta

# Configuração de Página
st.set_page_config(page_title="Predator Elite", layout="wide")

# Estilo Visual Minimalista (Mais leve)
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .card {
        background: linear-gradient(135deg, #c9a227 0%, #8e6d13 100%);
        padding: 15px; border-radius: 12px; color: black; 
        margin-bottom: 10px; text-align: center; border: 1px solid #fff;
    }
    </style>
    """, unsafe_allow_html=True)

API_TOKEN = "b8c288ff23ca4b2480f5d479176fc61f"
HEADERS = {'X-Auth-Token': API_TOKEN}

st.title("🏆 PREDATOR: FILÉ MIGNON")
st.sidebar.header("Menu de Elite")

LIGAS = {
    "Champions League 🇪🇺": 2001,
    "Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿": 2021,
    "Série A Brasil 🇧🇷": 2013,
    "La Liga Espanha 🇪🇸": 2014,
    "Serie A Itália 🇮🇹": 2019
}

liga_nome = st.sidebar.selectbox("Escolha a Liga:", list(LIGAS.keys()))
liga_id = LIGAS[liga_nome]

if st.button("🔥 ESCANEAR JOGOS DE HOJE"):
    url = f"https://api.football-data.org/v4/competitions/{liga_id}/matches"
    try:
        res = requests.get(url, headers=HEADERS)
        if res.status_code == 200:
            hoje = datetime.now().strftime('%Y-%m-%d')
            jogos = [j for j in res.json().get('matches', []) if j['utcDate'].startswith(hoje)]
            
            if not jogos:
                st.warning(f"Sem jogos de elite hoje para {liga_nome}. O filé mignon volta em breve!")
            else:
                for j in jogos:
                    casa = j['homeTeam']['name']
                    fora = j['awayTeam']['name']
                    # Hora Brasília
                    hr = (datetime.strptime(j['utcDate'], "%Y-%m-%dT%H:%M:%SZ") - timedelta(hours=3)).strftime('%H:%M')
                    
                    st.markdown(f"""
                        <div class="card">
                            <b>🕒 {hr} BRT</b><br>
                            <span style='font-size:18px;'>{casa} vs {fora}</span><br>
                            <b>🎯 PALPITE: Vitória {casa}</b>
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("Erro na API. Tente novamente em 1 minuto.")
    except:
        st.error("Erro de conexão.")

st.sidebar.info("O Predator filtra apenas as melhores ligas do mundo.")
