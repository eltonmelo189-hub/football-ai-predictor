import streamlit as st
import time

st.set_page_config(page_title="Predator Studio AI", layout="centered")

# Estilo Dark Gold (Igual aos apps de sinais caros)
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .resultado-box { 
        background: #1a1c23; padding: 25px; border-radius: 15px; 
        text-align: center; border: 2px solid #c9a227; margin-top: 20px;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #c9a227, #8e6d13);
        color: white; border: none; font-weight: bold; height: 50px; width: 100%;
    }
    .win-btn { background-color: #28a745 !important; }
    .loss-btn { background-color: #dc3545 !important; }
    </style>
    """, unsafe_allow_html=True)

# Inicializa o placar se não existir
if 'greens' not in st.session_state: st.session_state.greens = 0
if 'reds' not in st.session_state: st.session_state.reds = 0

def main():
    st.markdown("<h1 style='text-align: center; color: #c9a227;'>🏆 PREDATOR FOOTBALL STUDIO</h1>", unsafe_allow_html=True)
    
    # Placar de Lucro
    c1, c2 = st.columns(2)
    c1.metric("✅ GREENS (LUCRO)", st.session_state.greens)
    c2.metric("❌ REDS (PERDA)", st.session_state.reds)

    st.markdown("---")
    st.markdown("### 📊 Histórico Atual (C ou V):")
    col1, col2, col3, col4 = st.columns(4)
    r1 = col1.text_input("Último", "C").upper()
    r2 = col2.text_input("Penúlt.", "V").upper()
    r3 = col3.text_input("Antep.", "C").upper()
    r4 = col4.text_input("4º Atrás", "C").upper()

    if st.button("🔍 GERAR SINAL DE ENTRADA"):
        with st.status("🧠 Analisando algoritmos...", expanded=False):
            time.sleep(1)
        
        # Lógica de Análise Baseada em Padrões do Jogo
        if r1 == r2 == "C":
            sinal, cor, gale = "🔴 ENTRAR NO CASA", "#ff4b4b", "⚠️ Até GALE 2"
        elif r1 == r2 == "V":
            sinal, cor, gale = "🔵 ENTRAR NO VISITANTE", "#007bff", "⚠️ Até GALE 2"
        elif r1 != r2 and r2 != r3: # Padrão Xadrez
            sinal, cor, gale = "🔴 ENTRAR NO CASA", "#ff4b4b", "⚠️ Quebra de Xadrez"
        else:
            sinal, cor, gale = "⚖️ AGUARDAR", "#888", "Mesa instável"

        st.markdown(f"""
            <div class="resultado-box">
                <h1 style='color: {cor};'>{sinal}</h1>
                <p style='color: #c9a227;'>{gale}</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.write("🏁 **Resultado da última entrada:**")
    bc1, bc2 = st.columns(2)
    if bc1.button("✅ BATEU (GREEN)"):
        st.session_state.greens += 1
        st.rerun()
    if bc2.button("❌ ERROU (RED)"):
        st.session_state.reds += 1
        st.rerun()

if __name__ == "__main__":
    main()
