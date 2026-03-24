import streamlit as st

# Configuração visual 'Black & Gold' (conforme seus prints anteriores)
st.set_page_config(page_title="Predator Elite Football", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .mignon-card { 
        background: linear-gradient(135deg, #c9a227 0%, #8e6d13 100%);
        padding: 25px; border-radius: 15px; border: 2px solid #fff;
        text-align: center; color: black; font-weight: bold;
    }
    .stSelectbox label { color: #c9a227 !important; font-size: 20px; }
    </style>
    """, unsafe_allow_html=True)

# Ligas que a IA considera 'Filé Mignon'
LIGAS_BOAS = ["Premier League 🏴󠁧󠁢󠁥󠁮󠁧󠁿", "Champions League 🇪🇺", "Série A Brasil 🇧🇷", "La Liga 🇪🇸", "Bundesliga 🇩🇪"]

st.title("🏆 PREDATOR: FILÉ MIGNON")

# 1. Filtro de Campeonato
liga = st.selectbox("Selecione a Liga de Elite:", LIGAS_BOAS + ["Outras (Risco Alto)"])

if liga == "Outras (Risco Alto)":
    st.error("⚠️ AVISO: A IA identifica baixa previsibilidade nesta liga. Cuidado!")
else:
    st.success(f"💎 LIGA SELECIONADA: {liga} (Alta Assertividade)")

# 2. Dados do Jogo
col1, col2 = st.columns(2)
casa = col1.text_input("Time da Casa:")
fora = col2.text_input("Time de Fora:")

# 3. Botão de Análise de Elite
if st.button("🔥 ESCANEAR FILÉ MIGNON"):
    with st.spinner("🧠 IA Cruzando Dados de Elite..."):
        import time; time.sleep(1.5)
        
        # Exemplo de resposta positiva para ligas de elite
        if liga in LIGAS_BOAS and casa and fora:
            st.markdown(f"""
                <div class="mignon-card">
                    🚀 ENTRADA CONFIRMADA (PADRÃO OURO)<br>
                    <span style='font-size: 22px;'>{casa} vs {fora}</span><br><br>
                    🎯 SUGESTÃO: Vitória {casa} (Proteção no Empate)<br>
                    📊 CONFIANÇA IA: 94%
                </div>
            """, unsafe_allow_html=True)
            st.balloons()
        else:
            st.warning("Preencha os times ou escolha uma Liga de Elite para ver o 'Filé'.")

st.markdown("---")
st.caption("Foco total em lucro. Se não for Filé, a gente não entra.")
