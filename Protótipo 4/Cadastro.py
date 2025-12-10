import streamlit as st
import re
import os

# COR DE FUNDO DA PÁGINA.
st.markdown("""
<style>
.stApp {
    background-color: #DB8100; /* Laranja */
}
</style>
""", unsafe_allow_html=True)

# LOGO.
logo = "Protótipo 4/assets/daytoday.png"
st.write("Existe?", os.path.exists(logo))
st.image(logo, width=200)

# TÍTULO.
st.title("Bem-vindo à tela de cadastro do DayToDay☀️")
st.write("Para começar a utilizar o DayToDay☀️, preencha o formulário abaixo com suas informações. Os campos marcados com * são obrigatórios e garantem que seu cadastro seja concluído corretamente.")
st.write("Basta inserir seus dados, revisar as informações e clicar em Cadastrar para seguir para a próxima etapa.")

# INFORMAÇÕES DO USUÁRIO.
with st.form("cadastro_form"):
    st.session_state.nome_cliente = st.text_input("Digite seu nome*: ")
    senha = st.text_input("Senha*: ", type="password")
    
    botao_cadastro = st.form_submit_button("Cadastrar")

    if botao_cadastro:
        # VALIDAÇÕES.
        erros = []
        if not st.session_state.nome_cliente:
            erros.append("É necessário digitar seu nome.")
        elif not re.match("^[A-Za-zÀ-ú ]+$", st.session_state.nome_cliente):
            erros.append("O nome só pode conter letras e espaços.")
        
        if not senha:
            erros.append("É necessário digitar uma senha.")
        elif not re.match(r"^\d+$", senha):
            erros.append("A senha permite somente números.")

        # EXIBIR INVALIDAÇÕES.
        if erros:
            for erro in erros:
                st.write(erro)
        else:
            st.success(f"Usuário {st.session_state.nome_cliente} cadastrado com sucesso!")
        
        # SALVAR OS DADOS PARA A PRÓXIMA O LOGIN.
            st.session_state["usuario"] = st.session_state.nome_cliente
            st.session_state["senha"] = senha

        # IR PARA O LOGIN.
            st.switch_page("pages/Login.py")

# PORQUE ESCOLHER O PROJETO DayToDay.
st.markdown("# Organize sua rotina de forma simples e prática")
st.markdown("Com o **DayToDay**, você mantém suas tarefas em dia e transforma seu dia a dia em algo mais produtivo e leve.")

st.write("Motivo 1 para usar o DayToDay: Ter sua rotina organizada de forma simples e prática.")
st.write("Motivo 2 para usar o DayToDay: Aumenta sua produtividade cumprindo tarefas no tempo certo.")
st.write("Motivo 3 para usar o DayToDay: Personalizar suas listas e rotinas de acordo com seu estilo de vida.")
st.write("Motivo 4 para usar o DayToDay: Acompanhar seu progresso e se manter motivado diariamente.")

st.write("Motivo 5 para usar o DayToDay: Acessar suas tarefas de qualquer lugar, a qualquer momento.")




