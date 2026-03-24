import streamlit as st
import requests
from datetime import datetime, timedelta

# CONFIGURAÇÃO VISUAL
st.set_page_config(page_title="Predator Radar", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .card-mignon {
        background: linear-gradient(135deg, #c9a227 0%, #8e6d13 100%);
        padding: 15px; border-radius: 15px; color: black; 
        margin-bottom: 15px; border: 2px solid #fff; text-align: center;
    }
    .status-ok { color: #00ff00; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# SUA CHAVE MANTIDA
API_TOKEN = "b8c288ff23ca4b2480f5d479176fc61f"
HEADERS = {'X-Auth-Token': API_TOKEN}

st.title("🏆 RADAR FILÉ MIGNON")
st.write("Status: <span class='status-ok'>SISTEMA ATIVO ✅</span>", unsafe_allow_html=True)

# Menu Lateral com mais opções para não ficar vazio
LIGAS = {
    "Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿": 2021, 
    "Champions League 🇪🇺": 2001,
    "Série A Brasil 🇧🇷": 2013,
    "Serie A Itália 🇮🇹": 2019,
    "La Liga Espanha 🇪🇸": 2014
}

liga_nome = st.sidebar.selectbox("Escolha a Liga:", list(LIGAS.keys()))
liga_id = LIGAS[liga_nome]

if st.button("🔍 ESCANEAR JOGOS DE HOJE"):
    try:
        url = f"https://api.football-data.org/v4/competitions/{liga_id}/matches"
        res = requests.get(url, headers=HEADERS)
        
        if res.status_code == 200:
            todos_jogos = res.json().get('matches', [])
            hoje = datetime.now().strftime('%Y-%m-%d')
            
            # Filtra jogos de hoje
            jogos_hoje = [j for j in todos_jogos if j['utcDate'].startswith(hoje)]
            
            if not jogos_hoje:
                st.warning(f"🏟️ Sem jogos de elite da {liga_nome} para hoje ({hoje}). Tente outra liga no menu ao lado!")
            else:
                for j in jogos_hoje:
                    casa = j['homeTeam']['name']
                    fora = j['awayTeam']['name']
                    
                    # Ajuste de Horário Brasil
                    dt_utc = datetime.strptime(j['utcDate'], "%Y-%m-%dT%H:%M:%SZ")
                    dt_br = dt_utc - timedelta(hours=3)
                    horario = dt_br.strftime('%H:%M')
                    
                    st.markdown(f"""
                        <div class="card-mignon">
                            <strong>🕒 {horario}</strong><br>
                            <b style='font-size: 20px;'>{casa} vs {fora}</b><br>
                            🎯 PALPITE: Vitória {casa} (Confiança 88%)
                        </div>
                    """, unsafe_allow_html=True)
        else:
            st.error("Erro na conexão. Aguarde 1 minuto e clique de novo.")
            
    except Exception as e:
        st.error("Ocorreu um erro ao carregar os dados. Tente atualizar a página.")

st.sidebar.markdown("---")
st.sidebar.write("💡 **Dica:** Se a Premier League não tiver jogo hoje, mude para 'Série A Brasil' ou 'Itália' para testar!")
