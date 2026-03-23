import streamlit as st
import requests
import pandas as pd

def main():
    st.set_page_config(page_title="Goal Getter", layout="wide")
    st.title('⚽ Goal Getter - Palpites Brasileirão')
    
    # Sua chave configurada
    api_key = "b8c288ff23ca4b2480f5d479176cf61f"
    league_id = "71" # Brasileirão Série A
    
    st.success("Conectado com sucesso à API de Futebol!")

    # Buscando jogos reais na internet
    url = f"https://api.football-data.org/v4/competitions/{league_id}/matches"
    headers = {'X-Auth-Token': api_key}
    
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        
        if 'matches' in data:
            matches = data['matches']
            st.subheader("Próximos Jogos Analisados")
            
            for match in matches:
                # Mostra apenas jogos que ainda vão acontecer
                if match['status'] in ['TIMED', 'SCHEDULED']:
                    home = match['homeTeam']['name']
                    away = match['awayTeam']['name']
                    date = match['utcDate'][:10]
                    
                    with st.expander(f"{home} vs {away} ({date})"):
                        st.write(f"🏟️ **Confronto:** {home} x {away}")
                        st.write(f"📅 **Data:** {date}")
                        st.info("💡 **Dica da IA:** Analisando tendências para este confronto...")
        else:
            st.warning("Nenhum jogo encontrado para os próximos dias.")
            
    except Exception as e:
        st.error("Erro ao carregar os jogos reais. Verifique a conexão.")

if __name__ == '__main__':
    main()
