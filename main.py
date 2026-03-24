import streamlit as st
import requests

# CONFIGURAÇÃO VISUAL PREMIUN
st.set_page_config(page_title="Predator Elite Radar", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .card-mignon {
        background: linear-gradient(135deg, #c9a227 0%, #8e6d13 100%);
        padding: 20px; border-radius: 15px; color: black; 
        margin-bottom: 15px; border: 2px solid #fff;
    }
    .status-api { color: #00ff00; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# CONFIGURAÇÃO DA SUA API (TOKEN QUE VOCÊ RECEBEU)
API_TOKEN = "b8c288ff23ca4b2480f5d479176fc61f"
HEADERS = {'X-Auth-Token': API_TOKEN}

st.title("🏆 RADAR FILÉ MIGNON: AUTOMÁTICO")
st.markdown(f"Status: <span class='status-api'>CONECTADO AO SATÉLITE ✅</span>", unsafe_allow_html=True)

# Filtro de Ligas de Elite (IDs da football-data.org)
# 2021 = Premier League | 2001 = Champions League
LIGAS = {"Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿": 2021, "Champions League 🇪🇺": 2001}

liga_nome = st.sidebar.selectbox("Escolha a Liga de Elite:", list(LIGAS.keys()))
liga_id = LIGAS[liga_nome]

if st.button("🔥 ESCANEAR PRÓXIMOS JOGOS"):
    with st.spinner("🧠 IA Analisando calendário de elite..."):
        url = f"https://api.football-data.org/v4/competitions/{liga_id}/matches?status=SCHEDULED"
        response = requests.get(url, headers=HEADERS)
        
        if response.status_code == 200:
            dados = response.json()
            jogos = dados.get('matches', [])[:5] # Pega os próximos 5 jogos
            
            if not jogos:
                st.info("Nenhum jogo programado para os próximos dias nesta liga.")
            
            for jogo in jogos:
                casa = jogo['homeTeam']['name']
                fora = jogo['awayTeam']['name']
                data_jogo = jogo['utcDate'].split('T')[0]
                
                st.markdown(f"""
                    <div class="card-mignon">
                        <small>📅 Data: {data_jogo}</small><br>
                        <strong style='font-size: 20px;'>{casa} vs {fora}</strong><br>
                        🎯 ANALISANDO... (Selecione para ver palpite)
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Erro ao conectar. Verifique se o plano grátis está ativo.")

st.sidebar.markdown("---")
st.sidebar.write("✅ Filtro: Ligas de Elite")
st.sidebar.write("📊 Fonte: Football-Data.org")
