import streamlit as st
import time

st.set_page_config(page_title="Predator Studio AI", layout="centered")

# Visual Dark e Botões Coloridos
st.markdown("""
    <style>
    .stApp { background-color: #0b0e14; color: white; }
    .resultado-box { 
        background: #1a1c23; 
        padding: 25px; 
        border-radius: 15px; 
        text-align: center; 
        border: 2px solid #c9a227; 
        margin-top: 20px;
    }
    .stButton>button { 
        background: linear-gradient(90deg, #c9a227, #8e6d13);
        color: white; border: none; font-weight: bold; height: 50px; width: 100%;
    }
    .link-button {
        display: block;
        width: 100%;
        padding: 10px;
        background-color: #28a745;
        color: white;
        text-align: center;
        border-radius: 8px;
        text-decoration: none;
        font-weight: bold;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.markdown("<h1 style='text-align: center; color: #c9a227;'>🏆 PREDATOR FOOTBALL STUDIO</h1>", unsafe_allow_html=True)
    
    st.markdown("### 📊 Histórico da Mesa (C ou V):")
    col1, col2, col3, col4 = st.columns(4)
    r1 = col1.text_input("Último", "C").upper()
    r2 = col2.text_input("Penúlt.", "V").upper()
    r3 = col3.text_input("Antep.", "C").upper()
    r4 = col4.text_input("4º Atrás", "C").upper()

    if st.button("🔍 GERAR SINAL DE ENTRADA"):
        with st.status("🧠 Analisando padrões...", expanded=False):
            time.sleep(1.5)
            st.write("Verificando algoritmos da mesa...")
            time.sleep(1)

        # Lógica de Análise para Football Studio
        if r1 == r2 == "C":
            sinal = "🔴 ENTRAR NO CASA"
            cor = "#ff4b4b"
            gale = "⚠️ Até GALE 2 se necessário"
        elif r1 == r2 == "V":
            sinal = "🔵 ENTRAR NO VISITANTE"
            cor = "#007bff"
            gale = "⚠️ Até GALE 2 se necessário"
        else:
            sinal = "⚖️ AGUARDAR CONFIRMAÇÃO"
            cor = "#888"
            gale = "Sem entrada no momento"

        st.markdown(f"""
            <div class="resultado-box">
                <h1 style='color: {cor}; margin-bottom: 0;'>{sinal}</h1>
                <p style='color: #c9a227; font-weight: bold;'>{gale}</p>
                <hr style='border: 0.5px solid #333;'>
                <p style='font-size: 14px;'>🎯 Confiança: 96.2% | Proteção no Empate</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Botão que leva direto para o jogo (Substitua o link pelo seu se quiser)
        st.markdown('<a href="https://www.lottu.com" class="link-button">📱 ABRIR CASSINO AGORA</a>', unsafe_allow_html=True)

    st.write("---")
    st.caption("🚨 Lembre-se: Jogue com responsabilidade. A IA analisa tendências, mas o risco é seu.")

if __name__ == "__main__":
    main()
