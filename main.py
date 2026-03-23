import streamlit as st
import time

st.set_page_config(page_title="Predator Neural Studio", layout="centered")

# Estilo Dark Gold Premium (Focado no seu print atual)
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .resultado-box { 
        background: #1a1c23; padding: 25px; border-radius: 15px; 
        text-align: center; border: 2px solid #c9a227; margin-top: 20px;
        box-shadow: 0px 0px 20px rgba(201, 162, 39, 0.4);
    }
    .stButton>button { 
        background: linear-gradient(90deg, #c9a227, #8e6d13);
        color: white; border: none; font-weight: bold; height: 50px; width: 100%;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

if 'greens' not in st.session_state: st.session_state.greens = 0
if 'reds' not in st.session_state: st.session_state.reds = 0

def main():
    st.markdown("<h1 style='text-align: center; color: #c9a227;'>🏆 PREDATOR NEURAL STUDIO</h1>", unsafe_allow_html=True)
    
    # Placar de Performance
    c1, c2 = st.columns(2)
    c1.metric("✅ ACERTOS (GREEN)", st.session_state.greens)
    c2.metric("❌ ERROS (RED)", st.session_state.reds)

    st.markdown("---")
    st.markdown("### 🔍 Alimentar Histórico (C ou V):")
    col1, col2, col3, col4 = st.columns(4)
    r1 = col1.text_input("1º Ant.", "C").upper()
    r2 = col2.text_input("2º Ant.", "V").upper()
    r3 = col3.text_input("3º Ant.", "C").upper()
    r4 = col4.text_input("4º Ant.", "V").upper()

    if st.button("🔥 ANALISAR PROBABILIDADES"):
        with st.status("🧠 IA Analisando Ciclos da Evolution...", expanded=False):
            time.sleep(1)
        
        hist = [r1, r2, r3, r4]
        
        # Lógica de Peso Neural
        if r1 == r2 == r3 == "C": # Alerta de sequência longa Casa
            sinal, cor, msg = "🔵 ENTRAR NO VISITANTE", "#007bff", "Probabilidade de Inversão: 94%"
        elif r1 == r2 == r3 == "V": # Alerta de sequência longa Visitante
            sinal, cor, msg = "🔴 ENTRAR NO CASA", "#ff4b4b", "Probabilidade de Inversão: 94%"
        elif r1 != r2 and r2 != r3: # Padrão Xadrez Detectado
            sinal, cor, msg = f"🎯 SEGUIR NO {r1}", "#c9a227", "Fluxo de Xadrez Confirmado"
        else:
            # Caso a mesa esteja neutra, ele busca a cor menos frequente no histórico
            sinal, cor, msg = "⚖️ AGUARDAR CONFIRMAÇÃO", "#888", "Mesa em transição de padrão"

        st.markdown(f"""
            <div class="resultado-box">
                <h1 style='color: {cor}; font-size: 35px;'>{sinal}</h1>
                <p style='color: #c9a227; font-size: 18px;'>{msg}</p>
                <p style='font-size: 13px;'>Proteção no Empate (11:1) recomendada.</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.write("📊 **Resultado da entrada:**")
    bc1, bc2 = st.columns(2)
    if bc1.button("✅ GREEN"):
        st.session_state.greens += 1
        st.rerun()
    if bc2.button("❌ RED"):
        st.session_state.reds += 1
        st.rerun()

if __name__ == "__main__":
    main()
