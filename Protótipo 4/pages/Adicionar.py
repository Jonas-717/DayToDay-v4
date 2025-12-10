import streamlit as st
from datetime import datetime


# I N I C I A L I Z A Ç Ã O    D E    E S T A D O S

if "etapa" not in st.session_state:
    st.session_state.etapa = 0

# dados temporários da atividade sendo cadastrada
if "atividade_temp" not in st.session_state:
    st.session_state.atividade_temp = ""
if "descricao_temp" not in st.session_state:
    st.session_state.descricao_temp = ""
if "prazo_temp" not in st.session_state:
    st.session_state.prazo_temp = ""
if "prioridade_temp" not in st.session_state:
    st.session_state.prioridade_temp = ""

# listas permanentes usadas pelo MENU
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
h1, h2, h3, p, label {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)


# T Í T U L O
st.markdown("<h1>Bem-Vindo ao DayToDay ⛅ !</h1>", unsafe_allow_html=True)
st.write("Você é novo aqui? Então vamos começar!")


# --------------------------------| A T I V I D A D E S |-------------------------------------------------------------

# N O M E  (0)

if st.session_state.etapa == 0:

    st.markdown("<h3>Digite sua primeira atividade :</h3>", unsafe_allow_html=True)
    st.session_state.atividade_temp = st.text_input("Nome", value=st.session_state.atividade_temp)

    if st.button("Pronto!"):
        if st.session_state.atividade_temp.strip() != "":
            st.success("Tarefa adicionada com sucesso!")
            st.session_state.etapa = 1
        else:
            st.warning("Digite um nome válido!")

    st.stop()


# D E S C R I Ç Ã O  (1)

if st.session_state.etapa == 1:

    st.markdown("<h3>Digite a descrição:</h3>", unsafe_allow_html=True)
    st.session_state.descricao_temp = st.text_input("Descrição", value=st.session_state.descricao_temp)

    if st.button("Pronto"):
        if st.session_state.descricao_temp.strip() != "":
            st.success("Descrição adicionada!")
            st.session_state.etapa = 2
        else:
            st.warning("Digite uma descrição válida!")

    st.stop()


# P R A Z O  (Prazo: HH:MM)  (2)

if st.session_state.etapa == 2:

    st.markdown("<h3>Agora digite o prazo (em horas — ex: 15:00):</h3>", unsafe_allow_html=True)
    st.session_state.prazo_temp = st.text_input("Prazo (HH:MM)", value=st.session_state.prazo_temp)

    if st.button("Confirmar prazo"):
        try:
            datetime.strptime(st.session_state.prazo_temp, "%H:%M")
            st.success("Prazo registrado!")
            st.session_state.etapa = 3
        except ValueError:
            st.warning("Digite o horário no formato HH:MM (exemplo: 15:00).")

    st.stop()


# P R I O R I D A D E  (3)

if st.session_state.etapa == 3:

    st.markdown("<h3>Agora adicione a prioridade:</h3>", unsafe_allow_html=True)
    st.session_state.prioridade_temp = st.radio(
        "",
        ["Baixa", "Média", "Alta"],
        index=["Baixa", "Média", "Alta"].index(st.session_state.prioridade_temp)
        if st.session_state.prioridade_temp else 0
    )

    if st.button("Confirmar"):
        st.success("Prioridade registrada!")
        st.session_state.etapa = 4

    st.stop()


# F I N A L I Z A Ç Ã O   e   S A L V A M E N T O  (4)

if st.session_state.etapa == 4:

    st.markdown("<h2 style='color:lightgreen;'>Perfeito! 🎉</h2>", unsafe_allow_html=True)

    st.subheader(f"- **Atividade:** {st.session_state.atividade_temp}")
    st.subheader(f"- **Descrição:** {st.session_state.descricao_temp}")
    st.subheader(f"- **Prazo:** {st.session_state.prazo_temp}")
    st.subheader(f"- **Prioridade:** {st.session_state.prioridade_temp}")

    st.write("---")

    st.markdown("### Deseja salvar esta atividade?")

    if st.button("Salvar e voltar ao menu"):

        # adiciona atividade formatada (compatível com o MENU)
        nova_atividade = (
            f"{st.session_state.atividade_temp} • {st.session_state.descricao_temp} • "
            f"Prazo: {st.session_state.prazo_temp} • Prioridade: {st.session_state.prioridade_temp}"
        )

        st.session_state.atividades.append(nova_atividade)
        st.session_state.status_atividades.append("Pendente")

        # reset do cadastro
        st.session_state.etapa = 0
        st.session_state.atividade_temp = ""
        st.session_state.descricao_temp = ""
        st.session_state.prazo_temp = ""
        st.session_state.prioridade_temp = ""

        st.switch_page("pages/Menu Principal.py")

    if st.button("Cancelar"):
        st.session_state.etapa = 0
        st.switch_page("pages/Menu Principal.py")

