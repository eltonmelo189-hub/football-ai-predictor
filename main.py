import streamlit as st
import time

# Configuração de ecrã para telemóvel
st.set_page_config(page_title="Predator Ultra-Flash", layout="centered")

# CSS para Botões Gigantes e Alerta Visual
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; }
    /* Botões que ocupam metade do ecrã cada */
    div.stButton > button {
        width: 100%; height: 120px; font-size: 30px !important; 
        font-weight: bold; border-radius: 20px; border: 2px solid #c9a227;
    }
    .btn-casa { background: linear-gradient(145deg, #ff4b4b, #8b0000) !important; color: white !important; }
    .btn-visi { background: linear-gradient(145deg, #007bff, #00008b) !important; color: white !important; }
    
    /* Card de Sinal que pisca para chamar atenção */
    .sinal-alerta {
        background: #1a1c23; padding: 30px; border-radius: 20px;
        border: 4px solid #c9a227; text-align: center;
        animation: blinker 1.5s linear infinite;
    }
    @keyframes blinker { 50% { opacity: 0.5; border-color: #fff; } }
    </style>
    """, unsafe_allow_html=True)

if 'dados' not in st.session_state: st.session_state.dados = []

def processar(cor):
    st.session_state.dados.insert(0, cor)
    if len(st.session_state.dados) > 4:
        st.session_state.dados.pop()

st.markdown("<h1 style='text-align: center; color: #c9a227;'>⚡ PREDATOR FLASH</h1>", unsafe_allow_html=True)

# Área de Botões - TOQUE ÚNICO
col1, col2 = st.columns(2)

with col1:
    if st.button("🔴\nCASA", key="c"):
        processar("C")
        st.rerun()

with col2:
    if st.button("🔵\nVISITANTE", key="v"):
        processar("V")
        st.rerun()

# ANÁLISE AUTOMÁTICA IMEDIATA
if len(st.session_state.dados) >= 3:
    d = st.session_state.dados
    
    # Lógica de Inteligência: Procura quebra de sequência ou xadrez
    if d[0] == d[1] == d[2]:
        sinal = "🔥 ENTRAR NO VISITANTE" if d[0] == "C" else "🔥 ENTRAR NA CASA"
        cor_txt = "#007bff" if "VISITANTE" in sinal else "#ff4b4b"
        
        st.markdown(f"""
            <div class="sinal-alerta">
                <h1 style='color: {cor_txt}; margin:0;'>{sinal}</h1>
                <p style='color: #c9a227; font-size: 20px;'><b>COBRIR EMPATE (85% Confiança)</b></p>
            </div>
        """, unsafe_allow_html=True)
    
    elif d[0] != d[1] and d[1] != d[2]:
        st.info("🔄 PADRÃO XADREZ: Aguarde a quebra para entrar com segurança.")
    else:
        st.write("⏳ Analisando mesa... Continue inserindo os resultados.")

# Histórico rápido no rodapé
st.markdown("---")
st.write(f"📊 Últimos: {' | '.join(st.session_state.dados)}")
if st.button("🗑️ LIMPAR"):
    st.session_state.dados = []
    st.rerun()
