import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Predator Neural", layout="centered")

# Estilo para botões gigantes e fáceis de clicar
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; }
    div.stButton > button {
        width: 100%; height: 80px; font-size: 24px !important; font-weight: bold;
        border-radius: 15px; margin-bottom: 10px;
    }
    .btn-casa { background-color: #ff4b4b !important; color: white !important; }
    .btn-visi { background-color: #007bff !important; color: white !important; }
    .status-box { 
        background: #1a1c23; padding: 20px; border: 2px solid #c9a227; 
        border-radius: 15px; text-align: center; font-size: 22px;
    }
    </style>
    """, unsafe_allow_html=True)

# Lista para guardar os últimos 4 resultados
if 'historico' not in st.session_state: st.session_state.historico = []

def adicionar_resultado(res):
    st.session_state.historico.insert(0, res)
    if len(st.session_state.historico) > 4:
        st.session_state.historico.pop()

st.markdown("<h2 style='text-align: center; color: #c9a227;'>🏆 PREDATOR SPEED</h2>", unsafe_allow_html=True)

# Histórico Visual (Bolinhas)
cols = st.columns(4)
for i in range(4):
    val = st.session_state.historico[i] if i < len(st.session_state.historico) else "-"
    cols[i].markdown(f"<div style='text-align:center; font-size:25px;'>{val}</div>", unsafe_allow_html=True)

st.markdown("---")

# BOTÕES DE ENTRADA RÁPIDA
st.write("👉 **Toque no que saiu agora no jogo:**")
c1, c2 = st.columns(2)

if c1.button("🔴 CASA", key="btn_c"):
    adicionar_resultado("C")
    st.rerun()

if c2.button("🔵 VISITANTE", key="btn_v"):
    adicionar_resultado("V")
    st.rerun()

# ANÁLISE AUTOMÁTICA (Sem precisar clicar em outro botão)
if len(st.session_state.historico) >= 3:
    h = st.session_state.historico
    # Exemplo de lógica: Se sair 3 iguais, ele manda inverter
    if h[0] == h[1] == h[2]:
        sinal = "🔥 ENTRAR NO VISITANTE" if h[0] == "C" else "🔥 ENTRAR NA CASA"
        cor_sinal = "#ff4b4b" if "CASA" in sinal else "#007bff"
    else:
        sinal = "⚖️ AGUARDAR PADRÃO"
        cor_sinal = "#888"
    
    st.markdown(f"<div class='status-box' style='color:{cor_sinal};'><b>{sinal}</b><br><small>Proteja o Empate</small></div>", unsafe_allow_html=True)

if st.button("🗑️ LIMPAR TUDO"):
    st.session_state.historico = []
    st.rerun()
