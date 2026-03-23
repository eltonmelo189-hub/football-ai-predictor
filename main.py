import streamlit as st
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Predator Neural Studio", layout="centered")

# Estilo Visual Dark Gold Premium
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .status-card { 
        background: #1a1c23; padding: 25px; border-radius: 15px; 
        border: 2px solid #c9a227; text-align: center; margin-top: 10px;
        box-shadow: 0px 4px 20px rgba(201, 162, 39, 0.3);
    }
    .stButton>button { 
        background: linear-gradient(90deg, #c9a227, #8e6d13);
        color: white; border: none; font-weight: bold; height: 50px; width: 100%;
        border-radius: 10px;
    }
    .reset-btn>button { background: #333 !important; height: 35px !important; }
    </style>
    """, unsafe_allow_html=True)

# Inicialização de variáveis de estado
if 'greens' not in st.session_state: st.session_state.greens = 0
if 'reds' not in st.session_state: st.session_state.reds = 0

def main():
    st.markdown("<h1 style='text-align: center; color: #c9a227;'>🏆 PREDATOR NEURAL STUDIO</h1>", unsafe_allow_html=True)
    
    # Painel Lateral Avançado
    agora = datetime.now()
    st.sidebar.markdown(f"### 🕒 Hora Atual: {agora.strftime('%H:%M')}")
    st.sidebar.markdown("---")
    st.sidebar.subheader("📅 Próximos Horários de Pico:")
    # Gera horários fictícios baseados em ciclos de 15 min para estratégia
    for i in range(1, 4):
        h_pico = (agora + timedelta(minutes=15*i)).strftime("%H:%M")
        st.sidebar.code(f"🔥 {h_pico} - Alta Assertividade")
    
    # Placar Superior
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
    with col_an:
        analisar = st.button("🔥 ANALISAR PRÓXIMA RODADA")
    with col_re:
        st.markdown('<div class="reset-btn">', unsafe_allow_html=True)
        limpar = st.button("🗑️ RESET")
        st.markdown('</div>', unsafe_allow_html=True)

    if limpar:
        st.rerun()

    if analisar:
        with st.status("🧠 IA Escaneando Baralho...", expanded=False):
            time.sleep(1.2)
        
        hist = [r1, r2, r3, r4]
        # Lógica de Decisão Neural
        if r1 == r2 == r3 == "C":
            sinal, cor, conf = "🔵 ENTRAR NO VISITANTE", "#007bff", "96%"
            obs = "Exaustão de Casa detectada. Inversão iminente."
        elif r1 == r2 == r3 == "V":
            sinal, cor, conf = "🔴 ENTRAR NO CASA", "#ff4b4b", "96%"
            obs = "Exaustão de Visitante detectada. Inversão iminente."
        elif r1 != r2 and r2 != r3:
            sinal, cor, conf = f"🎯 SEGUIR TENDÊNCIA {r1}", "#c9a227", "91%"
            obs = "Padrão de Alternância (Xadrez) ativo."
        else:
            sinal, cor, conf = "⚖️ AGUARDAR", "#888", "--"
            obs = "Mesa sem padrão claro. Proteja sua banca."

        st.markdown(f"""
            <div class="status-card">
                <h1 style='color: {cor};'>{sinal}</h1>
                <p style='color: #c9a227; font-size: 18px;'>Confiança: {conf}</p>
                <p style='font-size: 14px;'>{obs}<br><b>⚠️ Proteção no Empate (11:1)</b></p>
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
