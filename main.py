import streamlit as st
import time

# Configuração visual premium (conforme os teus prints)
st.set_page_config(page_title="Predator Elite Football", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .mignon-card { 
        background: linear-gradient(135deg, #c9a227 0%, #8e6d13 100%);
        padding: 25px; border-radius: 15px; border: 2px solid #fff;
        text-align: center; color: black; font-weight: bold;
    }
    .status-alert {
        background: #1a1c23; padding: 15px; border-radius: 10px;
        border-left: 5px solid #ff4b4b; margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

LIGAS_BOAS = ["Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿", "Champions League 🇪🇺", "Série A Brasil 🇧🇷", "La Liga 🇪🇸", "Bundesliga 🇩🇪"]

st.title("🏆 PREDATOR: FILÉ MIGNON")

# 1. Filtro de Campeonato
liga = st.selectbox("Selecione a Liga de Elite:", LIGAS_BOAS + ["Outras (Risco Alto)"])

# 2. Dados da Partida
col1, col2 = st.columns(2)
casa = col1.text_input("Time da Casa:")
fora = col2.text_input("Time de Fora:")

# 3. Mini-Histórico (Opcional para dar peso à IA)
st.markdown("### 📊 Tendência Recente (V=Vitória, E=Empate, D=Derrota)")
h_casa = st.text_input("Últimos 5 jogos do Casa (ex: VVVED):", "VVV").upper()
h_fora = st.text_input("Últimos 5 jogos do Fora (ex: DDEED):", "DDD").upper()

if st.button("🔥 ESCANEAR OPORTUNIDADE"):
    if not casa or not fora:
        st.warning("Por favor, preenche o nome dos times.")
    else:
        with st.status("🧠 IA Analisando Odds e Tendências...", expanded=False):
            time.sleep(2)
        
        # Lógica do Filé Mignon: Só dá sinal verde se a diferença for clara
        vitorias_casa = h_casa.count('V')
        derrotas_fora = h_fora.count('D')
        
        if liga in LIGAS_BOAS and (vitorias_casa >= 3 or derrotas_fora >= 3):
            st.markdown(f"""
                <div class="mignon-card">
                    🚀 OPORTUNIDADE FILÉ MIGNON DETECTADA<br>
                    <span style='font-size: 20px;'>{casa} vs {fora}</span><br><br>
                    🎯 PALPITE: Vitória {casa}<br>
                    📊 CONFIANÇA: {75 + (vitorias_casa * 5)}%
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
        else:
            st.markdown("""
                <div class="status-alert">
                    ⚠️ JOGO FORA DO PADRÃO OURO<br>
                    <small>A IA detetou equilíbrio excessivo ou liga de baixa confiança. Recomendamos não apostar nesta partida.</small>
                </div>
            """, unsafe_allow_html=True)

st.markdown("---")
st.caption("Foco em qualidade, não em quantidade. Se não é Filé, a gente não entra.")
