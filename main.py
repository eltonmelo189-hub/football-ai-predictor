import streamlit as st
import time
from datetime import datetime, timedelta

st.set_page_config(page_title="Predator Neural Studio", layout="centered")

# Estilo Dark Gold Refinado
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
    </style>
    """, unsafe_allow_html=True)

if 'greens' not in st.session_state: st.session_state.greens = 0
if 'reds' not in st.session_state: st.session_state.reds = 0

def main():
    st.markdown("<h1 style='text-align: center; color: #c9a227;'>🏆 PREDATOR NEURAL STUDIO</h1>", unsafe_allow_html=True)
    
    # Barra Lateral com Horários (Como no seu print)
    agora = datetime.now()
    st.sidebar.markdown(f"### 🕒 Hora Atual: {agora.strftime('%H:%M')}")
    st.sidebar.markdown("---")
    st.sidebar.subheader("📅 Horários de Alta Assertividade:")
    for i in range(1, 4):
        h_pico = (agora + timedelta(minutes=12*i)).strftime("%H:%M")
        st.sidebar.warning(f"🔥 {h_pico} - Entrada Confirmada")

    # Placar de Resultados
    c1, c2 = st.columns(2)
    c1.metric("✅ GREENS", st.session_state.greens)
    c2.metric("❌ REDS", st.session_state.reds)

    st.markdown("### 🔍 Histórico Recente (C ou V):")
    col1, col2, col3, col4 = st.columns(4)
    r1 = col1.text_input("1º", "C").upper()
    r2 = col2.text_input("2º", "V").upper()
    r3 = col3.text_input("3º", "C").upper()
    r4 = col4.text_input("4º", "V").upper()

    col_an, col_re = st.columns([3, 1])
    if col_an.button("🔥 ANALISAR PROBABILIDADE"):
        with st.status("🧠 IA Analisando Ciclos...", expanded=False):
            time.sleep(1)
        
        # Lógica de Confiança Baseada no Padrão
        if r1 == r2 == r3:
            sinal, cor, conf = f"🔴 ENTRAR NO {'VISITANTE' if r1 == 'C' else 'CASA'}", "#ff4b4b", 97
            msg = "Quebra de Sequência Detectada!"
        elif r1 != r2 and r2 != r3:
            sinal, cor, conf = f"🔵 ENTRAR NO {r1}", "#007bff", 92
            msg = "Padrão Xadrez Confirmado."
        else:
            sinal, cor, conf = "⚖️ AGUARDAR MESA", "#888", 0
            msg = "Mesa instável no momento."

        if conf > 0:
            st.markdown(f"""
                <div class="status-card">
                    <h2 style='color: {cor};'>{sinal}</h2>
                    <p style='color: #c9a227;'><b>Confiança da IA: {conf}%</b></p>
                    <progress value="{conf}" max="100" style="width:100%;"></progress>
                    <p style='font-size: 14px; margin-top: 10px;'>{msg}<br>🛡️ Proteção no Empate</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Aguarde a mesa definir um padrão claro para reduzir o risco.")

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
