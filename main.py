import streamlit as st
import time

st.set_page_config(page_title="Predator Studio AI", layout="centered")

# Estilo Dark Gold Premium
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
    </style>
    """, unsafe_allow_html=True)

if 'greens' not in st.session_state: st.session_state.greens = 0
if 'reds' not in st.session_state: st.session_state.reds = 0

def main():
    st.markdown("<h1 style='text-align: center; color: #c9a227;'>🏆 PREDATOR FOOTBALL STUDIO</h1>", unsafe_allow_html=True)
    
    # Placar Superior
    c1, c2 = st.columns(2)
    c1.metric("✅ GREENS", st.session_state.greens)
    c2.metric("❌ REDS", st.session_state.reds)

    st.markdown("---")
    st.markdown("### 📊 Histórico da Mesa (C ou V):")
    col1, col2, col3, col4 = st.columns(4)
    r1 = col1.text_input("Último", "C").upper()
    r2 = col2.text_input("Penúlt.", "V").upper()
    r3 = col3.text_input("Antep.", "C").upper()
    r4 = col4.text_input("4º Atrás", "V").upper()

    if st.button("🔍 GERAR SINAL DE ENTRADA"):
        with st.status("🧠 IA Analisando Algoritmos...", expanded=False):
            time.sleep(1)
        
        # LÓGICA DE INTELIGÊNCIA DE PADRÕES:
        historico = [r1, r2, r3, r4]
        
        # 1. Identifica Sequência (Surf)
        if r1 == r2 == r3:
            sinal, cor = f"🔴 ENTRAR NO {'CASA' if r1 == 'V' else 'VISITANTE'}", "#ff4b4b"
            msg = "⚠️ Alerta de Quebra de Sequência!"
        # 2. Identifica Alternância (Xadrez)
        elif r1 != r2 and r2 != r3 and r3 != r4:
            sinal, cor = f"🔵 ENTRAR NO {r1}", "#007bff"
            msg = "⚡ Seguindo o fluxo de Xadrez"
        # 3. Padrão de Repetição Dupla
        elif r1 == r2 and r3 == r4:
            sinal, cor = f"🔴 ENTRAR NO {'VISITANTE' if r1 == 'C' else 'CASA'}", "#ff4b4b"
            msg = "🎯 Padrão 2-2 Detectado"
        else:
            sinal, cor = "⚖️ AGUARDAR CONFIRMAÇÃO", "#888"
            msg = "Mesa sem padrão claro no momento."

        st.markdown(f"""
            <div class="resultado-box">
                <h1 style='color: {cor};'>{sinal}</h1>
                <p style='color: #c9a227;'>{msg}</p>
                <p style='font-size: 12px;'>Proteção no Empate | Até Gale 1</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.write("🏁 **Resultado da última entrada:**")
    bc1, bc2 = st.columns(2)
    if bc1.button("✅ BATEU"):
        st.session_state.greens += 1
        st.rerun()
    if bc2.button("❌ ERROU"):
        st.session_state.reds += 1
        st.rerun()

if __name__ == "__main__":
    main()
