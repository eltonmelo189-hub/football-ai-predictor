import streamlit as st
import time

# Configurações de Design Premium
st.set_page_config(page_title="Predator Studio Pro", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .resultado-box { 
        background: #1a1c23; padding: 25px; border-radius: 15px; 
        text-align: center; border: 2px solid #c9a227; margin-top: 20px;
        box-shadow: 0px 0px 15px rgba(201, 162, 39, 0.3);
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
    st.markdown("<h1 style='text-align: center; color: #c9a227;'>🏆 PREDATOR NEURAL STUDIO</h1>", unsafe_allow_html=True)
    
    # Painel de Lucro Real
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
        with st.spinner('Escaneando padrões de cartas...'):
            time.sleep(1.2)
        
        # Lógica Neural de Ciclos
        if r1 == r2 == r3: # Identifica tentativa de quebra de sequência longa
            sinal, cor = f"🔴 ENTRAR NO {'CASA' if r1 == 'V' else 'VISITANTE'}", "#ff4b4b"
            aviso = "🚨 ALERTA: Possível quebra de sequência detectada!"
        elif r1 != r2 and r2 != r3: # Identifica padrão de alternância (Xadrez)
            sinal, cor = f"🔵 ENTRAR NO {r1}", "#007bff"
            aviso = "⚡ PADRÃO: Seguindo fluxo de alternância (Xadrez)."
        elif r1 == r2 and r3 == r4: # Padrão de repetição em duplas (2-2)
            sinal, cor = f"🔴 ENTRAR NO {'VISITANTE' if r1 == 'C' else 'CASA'}", "#ff4b4b"
            aviso = "🎯 ALVO: Inversão de padrão 2-2 confirmada."
        else:
            sinal, cor = "⚖️ AGUARDAR MESA", "#888"
            aviso = "Mesa sem padrão estatístico claro. Não entre agora."

        st.markdown(f"""
            <div class="resultado-box">
                <h1 style='color: {cor}; font-size: 38px;'>{sinal}</h1>
                <p style='color: #c9a227; font-size: 18px;'>{aviso}</p>
                <p style='font-size: 14px; color: #aaa;'>Cobrir EMPATE | Gestão: Até Gale 1</p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    st.write("📊 **Confirmar resultado da entrada:**")
    bc1, bc2 = st.columns(2)
    if bc1.button("✅ GREEN"):
        st.session_state.greens += 1
        st.rerun()
    if bc2.button("❌ RED"):
        st.session_state.reds += 1
        st.rerun()

if __name__ == "__main__":
    main()
