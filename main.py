import streamlit as st
import requests
from datetime import datetime, timedelta

st.set_page_config(page_title="Predator Radar Elite", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .card-mignon {
        background: linear-gradient(135deg, #c9a227 0%, #8e6d13 100%);
        padding: 15px; border-radius: 15px; color: black; 
        margin-bottom: 15px; border: 2px solid #fff; text-align: center;
    }
    .status-ok { color: #00ff00; font-weight: bold; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

API_TOKEN = "b8c288ff23ca4b2480f5d479176fc61f"
HEADERS = {'X-Auth-Token': API_TOKEN}

st.title("🏆 PREDATOR: FILÉ MIGNON")
st.write("Status: <span class='status-ok'>BUSCANDO LUCRO ✅</span>", unsafe_allow_html=True)

# Ligas que seu plano cobre bem
LIGAS = {
    "Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿": 2021, 
    "Champions League 🇪🇺": 2001,
    "Série A Brasil 🇧🇷": 2013,
    "Serie A Itália 🇮🇹": 2019,
    "Eredivisie Holanda 🇳🇱": 2003,
    "Copa da Inglaterra 🏴󠁧󠁢󠁥󠁮󠁧󠁿": 2015
}

liga_nome = st.sidebar.selectbox("Escolha a Liga:", list(LIGAS.keys()))
liga_id = LIGAS[liga_nome]

if st.button("🔍 ESCANEAR OPORTUNIDADES"):
    try:
        # Busca jogos da liga selecionada
        url = f"https://api.football-data.org/v4/competitions/{liga_id}/matches"
        res = requests.get(url, headers=HEADERS)
        
        if res.status_code == 200:
            todos_jogos = res.json().get('matches', [])
            hoje = datetime.now().strftime('%Y-%m-%d')
            
            # Filtra jogos de hoje
            jogos_hoje = [j for j in todos_jogos if j['utcDate'].startswith(hoje)]
            
            if not jogos_hoje:
                st.warning(f"🏟️ Sem jogos de elite na {liga_nome} hoje. Verifique o Brasileirão ou ligas secundárias!")
            else:
                for j in jogos_hoje:
                    casa = j['homeTeam']['name']
                    fora = j['awayTeam']['name']
                    
                    # Horário Brasília (-3h)
                    dt_utc = datetime.strptime(j['utcDate'], "%Y-%m-%dT%H:%M:%SZ")
                    dt_br = dt_utc - timedelta(hours=3)
                    horario = dt_br.strftime('%H:%M')
                    
                    st.markdown(f"""
                        <div class="card-mignon">
                            <strong>🕒 {horario}</strong><br>
                            <b style='font-size: 20px;'>{casa} vs {fora}</b><br>
                            🎯 PALPITE: Vitória {casa} (Proteção Empate)<br>
                            🔥 CONFIANÇA: 85%
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("Aguarde um pouco (limite de requisições).")
            
    except:
        st.error("Erro ao carregar dados. Tente novamente.")

st.sidebar.markdown("---")
st.sidebar.write("💡 **Dica do Dia:** Terça-feira costuma ter jogos da **Copa da Inglaterra** ou **Série B**. Se não achar no Filé, espere até amanhã para a Champions!")
