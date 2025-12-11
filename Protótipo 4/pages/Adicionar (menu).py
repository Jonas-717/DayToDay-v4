import streamlit as st
from datetime import datetime

# I N I C I A L I Z A Ç Ã O
if "etapa2" not in st.session_state:
    st.session_state.etapa2 = 0

if "atividade2" not in st.session_state:
    st.session_state.atividade2 = ""
if "descricao2" not in st.session_state:
    st.session_state.descricao2 = ""
if "prazo2" not in st.session_state:
    st.session_state.prazo2 = ""
if "prioridade2" not in st.session_state:
    st.session_state.prioridade2 = ""

# listas globais usadas no MENU
if "atividades" not in st.session_state:
    st.session_state.atividades = []
if "status_atividades" not in st.session_state:
    st.session_state.status_atividades = []


# F U N D O
st.markdown("""
<style>
.stApp {
    background-color: #DB8100;
}
h1, h2, h3, label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)


# T Í T U L O
st.markdown("<h1>Vamos lá denovo ⛅!</h1>", unsafe_allow_html=True)


# N O M E  (0)
if st.session_state.etapa2 == 0:

    st.markdown("<h3>Cadastro de nova atividade ⛅ :</h3>", unsafe_allow_html=True)
    st.session_state.atividade2 = st.text_input("Nome", value=st.session_state.atividade2)

    if st.button("Pronto!"):
        if st.session_state.atividade2.strip() != "":
            st.success("Tarefa adicionada com sucesso!")
            st.session_state.etapa2 = 1
        else:
            st.warning("Digite um nome válido!")

    st.stop()


# D E S C R I Ç Ã O   (1)
if st.session_state.etapa2 == 1:

    st.markdown("<h3>Digite a descrição:</h3>", unsafe_allow_html=True)
    st.session_state.descricao2 = st.text_input("Descrição", value=st.session_state.descricao2)

    if st.button("Pronto"):
        if st.session_state.descricao2.strip() != "":
            st.success("Descrição adicionada!")
            st.session_state.etapa2 = 2
        else:
            st.warning("Digite uma descrição válida!")

    st.stop()


# P R A Z O  (2)
if st.session_state.etapa2 == 2:

    st.markdown("<h3>Digite o prazo da tarefa (ex: 15:00):</h3>", unsafe_allow_html=True)
    st.session_state.prazo2 = st.text_input("Prazo (HH:MM)", value=st.session_state.prazo2)

    if st.button("Confirmar prazo"):
        try:
            datetime.strptime(st.session_state.prazo2, "%H:%M")
            st.success("Prazo registrado!")
            st.session_state.etapa2 = 3
        except ValueError:
            st.warning("Formato inválido! Use HH:MM (ex: 15:00).")

    st.stop()


# P R I O R I D A D E  (3)
if st.session_state.etapa2 == 3:

    st.markdown("<h3>Agora adicione a prioridade:</h3>", unsafe_allow_html=True)
    st.session_state.prioridade2 = st.radio(
        "",
        ["Baixa", "Média", "Alta"],
        index=["Baixa", "Média", "Alta"].index(st.session_state.prioridade2)
        if st.session_state.prioridade2 else 0
    )

    if st.button("Confirmar prioridade"):
        st.success("Prioridade registrada!")
        st.session_state.etapa2 = 4

    st.stop()


# F I N A L I Z A M E N T O   e   S A L V A M E N T O
if st.session_state.etapa2 == 4:

    st.markdown("<h2 style='color:lightgreen;'>Perfeito! 🎉</h2>", unsafe_allow_html=True)

    st.subheader(f"- **Atividade:** {st.session_state.atividade2}")
    st.subheader(f"- **Descrição:** {st.session_state.descricao2}")
    st.subheader(f"- **Prazo:** {st.session_state.prazo2}")
    st.subheader(f"- **Prioridade:** {st.session_state.prioridade2}")

    st.write("---")

    st.success("Salvando atividade...")

    # Montando atividade para o MENU
    nova = (
        f"{st.session_state.atividade2} • "
        f"{st.session_state.descricao2} • "
        f"Prazo: {st.session_state.prazo2} • "
        f"Prioridade: {st.session_state.prioridade2}"
    )

    st.session_state.atividades.append(nova)
    st.session_state.status_atividades.append("Pendente")

    # Resetar dados
    st.session_state.etapa2 = 0
    st.session_state.atividade2 = ""
    st.session_state.descricao2 = ""
    st.session_state.prazo2 = ""
    st.session_state.prioridade2 = ""

    # Ir para o MENU
    st.switch_page("pages/Menu Principal.py")

