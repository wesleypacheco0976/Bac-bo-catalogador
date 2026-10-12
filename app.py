import streamlit as st

# Configuração da página do painel
st.set_page_config(page_title="Catalogador Bac Bo ao Vivo", layout="centered")

st.title("🎲 Catalogador Bac Bo ao Vivo")
st.markdown("Registre os resultados da mesa em tempo real para acompanhar as estatísticas.")

# Inicializa o estado da sessão para guardar os dados enquanto a aba estiver aberta
if "historico" not in st.session_state:
    st.session_state.historico = []  # Lista para guardar os resultados

# Função para adicionar um resultado
def registrar(vencedor):
    st.session_state.historico.append({
        "vencedor": vencedor
    })

# --- PAINEL DE BOTÕES DE ENTRADA ---
st.subheader("Registrar Última Rodada")
col_b1, col_b2, col_b3 = st.columns(3)

with col_b1:
    if st.button("🔵 Vitória Azul", use_container_width=True):
        registrar("Azul")
with col_b2:
    if st.button("🔴 Vitória Vermelho", use_container_width=True):
        registrar("Vermelho")
with col_b3:
    if st.button("🤝 Empate (Tie)", use_container_width=True):
        registrar("Empate")

# Botão para limpar histórico
if st.button("Limpar Histórico / Reiniciar"):
    st.session_state.historico = []
    st.rerun()

st.divider()

# --- CÁLCULO DE ESTATÍSTICAS ---
total_rodadas = len(st.session_state.historico)

if total_rodadas > 0:
    vitorias_azul = sum(1 for r in st.session_state.historico if r["vencedor"] == "Azul")
    vitorias_vermelho = sum(1 for r in st.session_state.historico if r["vencedor"] == "Vermelho")
    empates = sum(1 for r in st.session_state.historico if r["vencedor"] == "Empate")

    perc_azul = (vitorias_azul / total_rodadas) * 100
    perc_vermelho = (vitorias_vermelho / total_rodadas) * 100
    perc_empate = (empates / total_rodadas) * 100

    # Exibição das Métricas Principais
    st.subheader("📊 Estatísticas Gerais")
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total", total_rodadas)
    m2.metric("Azul", f"{vitorias_azul} ({perc_azul:.1f}%)")
    m3.metric("Vermelho", f"{vitorias_vermelho} ({perc_vermelho:.1f}%)")
    m4.metric("Empates", f"{empates} ({perc_empate:.1f}%)")

    # --- HISTÓRICO RECENTE ---
    st.subheader("📜 Últimos Resultados")
    ultimos = st.session_state.historico[-15:][::-1]
    
    linhas_visuais = ""
    for r in ultimos:
        if r["vencedor"] == "Azul":
            linhas_visuais += "🔵 "
        elif r["vencedor"] == "Vermelho":
            linhas_visuais += "🔴 "
        else:
            linhas_visuais += "🤝 "
            
    st.markdown(f"### {linhas_visuais}")

else:
    st.info("Nenhum resultado registrado ainda. Clique em um dos botões acima conforme o jogo avançar.")
