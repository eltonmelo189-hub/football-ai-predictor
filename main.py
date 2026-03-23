import streamlit as st
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Predator Neural Studio", layout="centered")

# CSS Premium (Baseado nos seus prints recentes)
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

def main():
    st.markdown("<h1 style='text-align: center; color: #c9a227;'>🏆 PREDATOR NEURAL STUDIO</h1>", unsafe_allow_html=True)
    
    # Sidebar: Gestão, Horários e Metas
    agora = datetime.now()
    st.sidebar.markdown(f"### 🕒 Hora Atual: {agora.strftime('%H:%M')}")
    st.sidebar.markdown("---")
    
    st.sidebar.subheader("💰 Gestão de Banca")
    banca_total = st.sidebar.number_input("Saldo (R$):", value=100.0)
    meta_lucro = st.sidebar.number_input("Meta de Lucro (R$):", value=20.0)
    stop_loss = st.sidebar.number_input("Stop Loss (R$):", value=10.0)
    
    percentual = st.sidebar.slider("Risco por entrada %", 1, 5, 2)
    valor_entrada = banca_total * (percentual / 100)
    
    lucro_atual = (st.session_state.greens * valor_entrada) - (st.session_state.reds * valor_entrada)

    st.sidebar.markdown(f"""
        <div class="banca-box">
            <small>Resultado Atual:</small><br><b>R$ {lucro_atual:.2f}</b><br>
            <progress value="{max(0, lucro_atual)}" max="{meta_lucro}" style="width:100%;"></progress>
        </div>
    """, unsafe_allow_html=True)

    # Monitor de Segurança
    if lucro_atual >= meta_lucro:
        st.balloons()
        st.success("🎯 META ATINGIDA! Hora de sacar e descansar.")
        st.stop()
    elif lucro_atual <= -stop_loss:
        st.error("⚠️ STOP LOSS ATINGIDO. Volte amanhã com a mente fria.")
        st.stop()

    # Dashboard de Performance
    c1, c2 = st.columns(2)
    c1.metric("✅ GREENS", st.session_state.greens)
    c2.metric("❌ REDS", st.session_state.reds)

    st.markdown("### 🔍 Alimentar Histórico (C ou V):")
    col1, col2, col3, col4 = st.columns(4)
    r1 = col1.text_input("1º", "C").upper()
    r2 = col2.text_input("2º", "V").upper()
    r3 = col3.text_input("3º", "C").upper()
    r4 = col4.text_input("4º", "V").upper()

    col_an, col_re = st.columns([3, 1])
    if col_an.button("🔥 GERAR PREVISÃO NEURAL"):
        with st.status("🧠 IA Calculando Ciclos...", expanded=False):
            time.sleep(1)
        
        # Lógica de Análise (Exemplo de Padrão)
        if r1 == r2 == r3:
            sinal, cor, conf = f"ENTRAR NO {'VISITANTE' if r1 == 'C' else 'CASA'}", "#ff4b4b", 98
        elif r1 != r2 and r2 != r3:
            sinal, cor, conf = f"SEGUIR TENDÊNCIA {r1}", "#007bff", 91
        else:
            sinal, cor, conf = "AGUARDAR CONFIRMAÇÃO", "#888", 0

        if conf > 0:
            st.markdown(f"""
                <div class="status-card">
                    <h2 style='color: {cor};'>{sinal}</h2>
                    <p style='color: #c9a227;'>Confiança: {conf}% | Aposta: R$ {valor_entrada:.2f}</p>
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
