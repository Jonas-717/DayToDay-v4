import streamlit as st

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
st.image(logo, width=200)

# TÍTULO DA PÁGINA.
st.title("Bem vindo à tela de Login.")

# VERIFICAÇÃO SE EXISTE UM USUÁRIO.
if "usuario" not in st.session_state:
    st.write("Nenhum usuário cadastrado. Volte para a página anterior.")
    st.stop()

st.write("Para acessar o menu principal no DayToDay☀️, basta informar o nome de usuário e a senha cadastrados anteriormente. Certifique-se de digitar as informações corretamente para que possamos confirmar sua identidade e liberar o acesso ao sistema.")
st.write("ATENÇÃO: Caso ainda não tenha criado um cadastro, volte à página inicial e complete o formulário de registro. se já estiver tudo certo, preencha os campos abaixo e clique em Entrar para continuar")
# LOGIN.
st.session_state.nome_cliente = st.text_input("Digite seu nome")
senha_login = st.text_input("Digite sua senha", type="password")

if st.button("Entrar"):
    if st.session_state.nome_cliente == st.session_state.usuario and senha_login == st.session_state.senha:
        st.success("Login realizado com sucesso!")
        # Ir para Adicionar.py
        st.switch_page("pages/Adicionar.py")
    else:

        st.write("Usuário ou senha incorretos.")


