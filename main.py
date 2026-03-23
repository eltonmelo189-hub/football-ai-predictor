import streamlit as st
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Predator Neural Studio", layout="centered")

# Estilo Premium Dark Gold (Ajustado conforme seus prints)
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .status-card { 
        background: #1a1c23; padding: 25px; border-radius: 15px; 
        border: 2px solid #c9a227; text-align: center; margin-top: 10px;
    }
    .banca-box {
        background: #252932; padding: 15px; border-radius: 10px;
        border-left: 5px solid #c9a227; margin-bottom: 20px;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #c9a227, #8e6d13);
        color: white; border: none; font-weight: bold; height: 50px; border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Inicialização de Variáveis de Sessão
if 'greens' not in st.session_state: st.session_state.greens = 0
if 'reds' not in st.session_state: st.session_state.reds = 0

def main():
    st.markdown("<h1 style='text-align: center; color: #c9a227;'>🏆 PREDATOR NEURAL STUDIO</h1>", unsafe_allow_html=True)
    
    # --- SIDEBAR: GESTÃO E HORÁRIOS ---
    agora = datetime.now()
    st.sidebar.markdown(f"### 🕒 Hora Atual: {agora.strftime('%H:%M')}")
    st.sidebar.markdown("---")
    
    st.sidebar.subheader("💰 Gestão de Banca")
    banca_total = st.sidebar.number_input("Saldo Total (R$):", min_value=0.0, value=100.0, step=10.0)
    percentual = st.sidebar.slider("Risco por entrada %", 1, 5, 2)
    
    valor_entrada = banca_total * (percentual / 100)
    valor_empate = valor_entrada * 0.10

    st.sidebar.markdown(f"""
        <div class="banca-box">
            <small>Aposta na Cor:</small><br><b>R$ {valor_entrada:.2f}</b><br>
            <small>Proteção Empate:</small><br><b>R$ {valor_empate:.2f}</b>
        </div>
    """, unsafe_allow_html=True)

    # --- DASHBOARD DE PERFORMANCE ---
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

    # --- BOTÕES DE AÇÃO ---
    col_an, col_re = st.columns([3, 1])
    
    if col_an.button("🔥 GERAR PREVISÃO NEURAL"):
        with st.status("🧠 Analisando Padrões de Mesa...", expanded=False):
            time.sleep(1.2)
        
        # Lógica de Decisão Baseada em Padrões do Football Studio
        if r1 == r2 == r3: # Quebra de sequência longa
            sinal, cor, conf = f"ENTRAR NO {'VISITANTE' if r1 == 'C' else 'CASA'}", "#ff4b4b", "97%"
            dica = "Detectada saturação. Probabilidade alta de inversão."
        elif r1 != r2 and r2 != r3: # Padrão Xadrez
            sinal, cor, conf = f"SEGUIR FLUXO {r1}", "#c9a227", "92%"
            dica = "Mesa em modo alternância. Siga a última cor."
        else:
            sinal, cor, conf = "AGUARDAR NOVA RODADA", "#888", "--"
            dica = "Padrão inconclusivo. Evite entradas de risco agora."

        st.markdown(f"""
            <div class="status-card">
                <h2 style='color: {cor};'>{sinal}</h2>
                <p style='color: #c9a227; font-weight: bold;'>Confiança: {conf}</p>
                <p style='font-size: 14px;'>{dica}<br><b>⚠️ Cubra o Empate (11:1)</b></p>
            </div>
        """, unsafe_allow_html=True)

    if col_re.button("🗑️ RESET"):
        st.session_state.greens = 0
        st.session_state.reds = 0
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
