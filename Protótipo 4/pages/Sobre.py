import streamlit as st 
from datetime import date 

st.write(st.__version__) # Versão do StreamLit

def sobre_page():
    st.title("🗓️ DayToDay - Sobre o Sistema")

    # Verificar a data para exibir uma mensagem diferente.
    dia = date.today().day
    if dia < 10:
        st.info("⏱️ Comecinho do mês! Organização em alta!")
    elif dia < 20:
        st.info("⏳ Meio do mês - continue focado!")
    else:
        st.info("🚀 Final do mês, reta final das tarefas!")

    st.write("___")

    # FOR (listar integrantes).
    integrantes = ["Vivian Santos", "Jonas Alves", "Paulo Bryan Souza"]
    st.subheader("👥 Equipe de Desenvolvimento")
    for nome in integrantes:
        st.write(f"- {nome}")

    st.write("---")

    # Exibe contagem rápida do número de integrantes.
    st.subheader("🔢 Integrantes na equipe")
    contador = 0 
    while contador < len(integrantes):
        contador += 1
    st.write(f"Total: **{contador}** membros")

    st.write("---")

    # Informações resumidas.
    st.subheader("📔 Sobre o DayToDay")
    st.write("""
        O DayToDay é um sistema simples de organização pessoal criado para auxiliar o usuário a gerenciar tarefas do seu dia a dia.
        A ideia principal do projeto é tornar o processo de planejamento mais simples, rápido e acessível, permitindo que o usuário controle sua rotina de forma prática.
        Ele incentiva a organização e facilita o acompanhamento das atividades do dia a dia.
        O DayToDay permite visualizar tarefas, marcar como concluídas e acompanhar o progresso do usuário.
    """)

    st.subheader("🎯 Funcionalidades")
    st.write("""
        - Cadastro
        - Login
        - Sobre
        - Adicionar tarefas
        - Botão "Feito"
        - Contar tarefas pendentes
        - Menu para exibir informações
        - Campo de prazo
    """)

    st.subheader("👨‍🎓 Professor responsável")
    st.write("Sávio Cunha")

    st.subheader("🗓️ Data")
    st.write(f"{date.today().strftime('%d/%m/%y')}")

# Testar isolado.
if __name__ == "__main__":
    sobre_page()


if st.button("Voltar"):

    st.switch_page("pages/Menu Principal.py")
