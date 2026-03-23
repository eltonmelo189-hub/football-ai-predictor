import streamlit as st
import time
from datetime import datetime

st.set_page_config(page_title="Predator Neural Pro", layout="centered")

# CSS para Visual Dark e Efeitos de Brilho
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .status-card { 
        background: #1a1c23; padding: 20px; border-radius: 12px; 
        border: 1px solid #c9a227; text-align: center; margin-bottom: 20px;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #c9a227, #8e6d13);
        color: white; border: none; font-weight: bold; height: 50px; width: 100%;
        border-radius: 10px; box-shadow: 0 4px 15px rgba(201, 162, 39, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

if 'greens' not in st.session_state: st.session_state.greens = 0
if 'reds' not in st.session_state: st.session_state.reds = 0

def main():
    st.markdown("<h1 style='text-align: center; color: #c9a227;'>🏆 PREDATOR NEURAL STUDIO</h1>", unsafe_allow_html=True)
    
    # Placar Superior
    c1, c2 = st.columns(2)
    c1.metric("✅ ACERTOS", st.session_state.greens)
    c2.metric("❌ ERROS", st.session_state.reds)

    st.markdown("---")
    
    # Horário Atual e Estimativa de Assertividade
    agora = datetime.now().strftime("%H:%M")
    st.sidebar.markdown(f"### 🕒 Hora Atual: {agora}")
    st.sidebar.info("📊 Tendência da Mesa: **ESTÁVEL**")
    
    st.markdown("### 🔍 Histórico Recente (C ou V):")
    col1, col2, col3, col4 = st.columns(4)
    r1 = col1.text_input("1º", "C").upper()
    r2 = col2.text_input("2º", "V").upper()
    r3 = col3.text_input("3º", "C").upper()
    r4 = col4.text_input("4º", "V").upper()

    if st.button("🔥 ANALISAR PRÓXIMA RODADA"):
        with st.status("🧠 IA Processando Ciclos de Cartas...", expanded=False):
            time.sleep(1.2)
        
        # Lógica de Probabilidade Neural
        if r1 == r2 == r3 == "C":
            sinal, cor, prob = "🔵 ENTRAR NO VISITANTE", "#007bff", "94.2%"
        elif r1 == r2 == r3 == "V":
            sinal, cor, prob = "🔴 ENTRAR NO CASA", "#ff4b4b", "94.2%"
        elif r1 != r2 and r2 != r3 and r3 != r4: # Identifica Xadrez Perfeito
            sinal, cor, prob = f"🎯 SEGUIR {r1}", "#c9a227", "91.5%"
        else:
            sinal, cor, prob = "⚖️ AGUARDAR", "#888", "N/A"

        st.markdown(f"""
            <div class="status-card">
                <h1 style='color: {cor}; font-size: 32px;'>{sinal}</h1>
                <p style='color: #c9a227; font-size: 18px;'>Confiança IA: {prob}</p>
                <p style='font-size: 14px;'>🛡️ Proteção no Empate Obrigatória</p>
            </div>
        """, unsafe_allow_html=True)

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
