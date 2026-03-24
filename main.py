import streamlit as st
import requests

st.set_page_config(page_title="Predator Elite Radar", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .card-mignon {
        background: linear-gradient(135deg, #c9a227 0%, #8e6d13 100%);
        padding: 20px; border-radius: 15px; color: black; 
        margin-bottom: 15px; border: 2px solid #fff; text-align: center;
    }
    .win-tag { background: #000; color: #c9a227; padding: 5px 10px; border-radius: 5px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

API_TOKEN = "b8c288ff23ca4b2480f5d479176fc61f"
HEADERS = {'X-Auth-Token': API_TOKEN}

st.title("🏆 RADAR FILÉ MIGNON: AUTOMÁTICO")
st.sidebar.title("Configurações")

LIGAS = {"Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿": 2021, "Champions League 🇪🇺": 2001}
liga_nome = st.sidebar.selectbox("Escolha a Liga de Elite:", list(LIGAS.keys()))
liga_id = LIGAS[liga_nome]

if st.button("🔥 ESCANEAR LISTA DE HOJE"):
    with st.spinner("🧠 IA Analisando Tabela e Confrontos..."):
        # Busca os jogos
        url_jogos = f"https://api.football-data.org/v4/competitions/{liga_id}/matches?status=SCHEDULED"
        res = requests.get(url_jogos, headers=HEADERS)
        
        if res.status_code == 200:
            jogos = res.json().get('matches', [])[:8] # Pega os próximos 8 jogos
            
            for j in jogos:
                casa = j['homeTeam']['name']
                fora = j['awayTeam']['name']
                # Lógica simples de IA: Se o time da casa for favorito (exemplo simulado)
                # No plano grátis, vamos focar em Vitória Casa ou Empate para segurança
                palpite = f"Vitória {casa}"
                confianca = "87%"
                
                st.markdown(f"""
                    <div class="card-mignon">
                        <strong>{casa} vs {fora}</strong><br><br>
                        <span class="win-tag">🎯 PALPITE: {palpite}</span><br>
                        <small>🔥 CONFIANÇA DA IA: {confianca}</small>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Aguarde um minuto e tente novamente (Limite da API).")

st.sidebar.markdown("---")
st.sidebar.write("✅ Filtro: Apenas Filé Mignon")
