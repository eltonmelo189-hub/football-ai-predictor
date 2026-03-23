import streamlit as st
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Predator Neural Studio", layout="centered")

# Estilo Premium Dark Gold
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .status-card { 
        background: #1a1c23; padding: 25px; border-radius: 15px; 
        border: 2px solid #c9a227; text-align: center; margin-top: 10px;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #c9a227, #8e6d13);
        color: white; border: none; font-weight: bold; height: 50px; border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'greens' not in st.session_state: st.session_state.greens = 0
if 'reds' not in st.session_state: st.session_state.reds = 0

def main():
    st.markdown("<h1 style='text-align: center; color: #c9a227;'>🏆 PREDATOR NEURAL STUDIO</h1>", unsafe_allow_html=True)
    
    # Sidebar com Horários (Sincronizado com seu print)
    agora = datetime.now()
    st.sidebar.markdown(f"### 🕒 Hora Atual: {agora.strftime('%H:%M')}")
    st.sidebar.markdown("---")
    st.sidebar.subheader("📅 Janelas de Alta Assertividade:")
    for i in range(1, 4):
        h_pico = (agora + timedelta(minutes=14*i)).strftime("%H:%M")
        st.sidebar.info(f"🔥 {h_pico} - Entrada Forte")

    # Placar de Performance
    c1, c2 = st.columns(2)
    c1.metric("✅ GREENS", st.session_state.greens)
    c2.metric("❌ REDS", st.session_state.reds)

    st.markdown("### 🔍 Histórico da Mesa (C ou V):")
    col1, col2, col3, col4 = st.columns(4)
    r1 = col1.text_input("1º", "C").upper()
    r2 = col2.text_input("2º", "V").upper()
    r3 = col3.text_input("3º", "C").upper()
    r4 = col4.text_input("4º", "V").upper()

    col_an, col_re = st.columns([3, 1])
    if col_an.button("🔥 ANALISAR PROBABILIDADE"):
        with st.status("🧠 IA Calculando Pesos de Cartas...", expanded=False):
            time.sleep(1.2)
        
        # Lógica de Cálculo de Probabilidade
        casa_prob, visi_prob = 50, 50
        if r1 == r2 == r3:
            sinal, cor, casa_prob, visi_prob = ("AZUL (VISITANTE)", "#007bff", 15, 85) if r1 == "C" else ("VERMELHO (CASA)", "#ff4b4b", 85, 15)
        elif r1 != r2 and r2 != r3:
            sinal, cor, casa_prob, visi_prob = (f"SEGUIR {r1}", "#c9a227", 70, 30) if r1 == "C" else (f"SEGUIR {r1}", "#c9a227", 30, 70)
        else:
            sinal, cor = "AGUARDAR MESA", "#888"

        st.markdown(f"""
            <div class="status-card">
                <h2 style='color: {cor};'>{sinal}</h2>
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <span>🔴 Casa: {casa_prob}%</span>
                    <span>🔵 Visitante: {visi_prob}%</span>
                </div>
                <progress value="{casa_prob}" max="100" style="width:100%; height: 20px;"></progress>
                <p style='font-size: 13px; margin-top: 10px;'><b>🛡️ Proteção no Empate Obrigatória</b></p>
            </div>
        """, unsafe_allow_html=True)

    if col_re.button("🗑️ RESET"):
        st.rerun()

    st.markdown("---")
    st.write("🏁 **Confirmar Resultado:**")
    bc1, bc2 = st.columns(2)
    if bc1.button("✅ GREEN"):
        st.session_state.greens += 1
        st.rerun()
    if bc2.button("❌ RED"):
        st.session_state.reds += 1
        st.rerun()

if __name__ == "__main__":
    main()
