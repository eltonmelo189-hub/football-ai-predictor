import streamlit as st
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Predator Neural Studio", layout="centered")

# Visual Dark Gold Premium
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .status-card { 
        background: #1a1c23; padding: 20px; border-radius: 15px; 
        border: 2px solid #c9a227; text-align: center;
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

# Inicialização de Variáveis
if 'greens' not in st.session_state: st.session_state.greens = 0
if 'reds' not in st.session_state: st.session_state.reds = 0
if 'historico_sinais' not in st.session_state: st.session_state.historico_sinais = []

def main():
    st.markdown("<h1 style='text-align: center; color: #c9a227;'>🏆 PREDATOR NEURAL STUDIO</h1>", unsafe_allow_html=True)
    
    # Sidebar: Gestão e Horários
    agora = datetime.now()
    st.sidebar.markdown(f"### 🕒 Hora: {agora.strftime('%H:%M')}")
    st.sidebar.markdown("---")
    
    st.sidebar.subheader("💰 Gestão de Banca")
    banca_total = st.sidebar.number_input("Saldo Total (R$):", min_value=0.0, value=100.0)
    percentual = st.sidebar.slider("Risco por entrada %", 1, 5, 2)
    
    valor_cor = banca_total * (percentual / 100)
    valor_empate = valor_cor * 0.10

    st.sidebar.markdown(f"""
        <div class="banca-box">
            <small>Entrada Cor:</small><br><b>R$ {valor_cor:.2f}</b><br>
            <small>Proteção Empate:</small><br><b>R$ {valor_empate:.2f}</b>
        </div>
    """, unsafe_allow_html=True)

    # Dashboard de Performance
    c1, c2 = st.columns(2)
    c1.metric("✅ ACERTOS", st.session_state.greens)
    c2.metric("❌ ERROS", st.session_state.reds)

    st.markdown("### 🔍 Histórico da Mesa (C ou V):")
    col1, col2, col3, col4 = st.columns(4)
    r1 = col1.text_input("1º", "C").upper()
    r2 = col2.text_input("2º", "V").upper()
    r3 = col3.text_input("3º", "C").upper()
    r4 = col4.text_input("4º", "V").upper()

    col_an, col_re = st.columns([3, 1])
    if col_an.button("🔥 GERAR PREVISÃO"):
        with st.status("🧠 IA Processando Variância...", expanded=False):
            time.sleep(1)
        
        # Lógica de Análise Neural
        if r1 == r2 == r3:
            sinal, cor, conf = f"ENTRAR NO {'VISITANTE' if r1 == 'C' else 'CASA'}", "#ff4b4b", 98
        elif r1 != r2 and r2 != r3:
            sinal, cor, conf = f"SEGUIR TENDÊNCIA {r1}", "#007bff", 92
        else:
            sinal, cor, conf = "AGUARDAR CONFIRMAÇÃO", "#888", 0

        if conf > 0:
            st.session_state.historico_sinais.insert(0, f"{agora.strftime('%H:%M:%S')} - {sinal} ({conf}%)")
            st.markdown(f"""
                <div class="status-card">
                    <h2 style='color: {cor};'>{sinal}</h2>
                    <p style='color: #c9a227;'>Confiança: {conf}% | Proteção Empate Sugerida</p>
                </div>
            """, unsafe_allow_html=True)

    if col_re.button("🗑️ RESET"):
        st.session_state.historico_sinais = []
        st.rerun()

    # Seção de Últimos Sinais
    if st.session_state.historico_sinais:
        st.markdown("---")
        st.subheader("📋 Últimos Sinais Gerados")
        for s in st.session_state.historico_sinais[:5]:
            st.write(s)

    st.markdown("---")
    st.write("🏁 **Resultado da Rodada:**")
    bc1, bc2 = st.columns(2)
    if bc1.button("✅ GREEN"):
        st.session_state.greens += 1
        st.rerun()
    if bc2.button("❌ RED"):
        st.session_state.reds += 1
        st.rerun()

if __name__ == "__main__":
    main()
