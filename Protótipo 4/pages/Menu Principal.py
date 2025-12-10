import streamlit as st
from datetime import datetime

# I N I C I A L I Z A Ç Ã O

if "atividades" not in st.session_state:
    st.session_state.atividades = []

if "status_atividades" not in st.session_state:
    st.session_state.status_atividades = []

# Se não existir nome, define um padrão
if "nome_cliente" not in st.session_state:
    st.session_state.nome_cliente = "Usuário"


# FUNÇÃO DO BOTÃO

def marcar_como_feito(index):
    st.session_state.status_atividades[index] = "Feito"


# F U N D O

st.markdown("""
<style>
    .stApp {
        background-color: #DB8100;
    }
    p { font-size: 25px; color: white; }
    h4 { font-size: 50px; color: white; }
</style>
""", unsafe_allow_html=True)

# I M A G E M

col_esq, col_dir = st.columns([2, 2])
with col_dir:
    st.image("Protótipo 4/assets/daytoday.png", width=500)


# T Í T U L O

st.markdown(f"<h1>Olá {st.session_state.nome_cliente} 👤</h1>", unsafe_allow_html=True)
st.markdown("<h1>⬇️ ATIVIDADES ⬇️</h1>", unsafe_allow_html=True)


# P R A Z O   (Prazo: HH:MM)

def extrair_prazo(texto):
    try:
        partes = texto.split("•")
        for p in partes:
            p = p.strip()
            if p.lower().startswith("prazo:"):
                return p.replace("Prazo:", "").replace("prazo:", "").strip()
    except:
        return None
    return None


# E X I B I R    A T I V I D A D E S

if not st.session_state.atividades:
    st.markdown("<p>Nenhuma atividade cadastrada ainda.</p>", unsafe_allow_html=True)

else:
    for a, atividade in enumerate(st.session_state.atividades):

        prazo = extrair_prazo(atividade)
        status = st.session_state.status_atividades[a]

        # Cor padrão
        cor_texto = "white"
        borda = "none"

        # -------------- LÓGICA DO PRAZO (VERSÃO FINAL CORRIGIDA) --------------

        if prazo:
            try:
                # Hora atual sem segundos e microssegundos
                agora = datetime.now().replace(second=0, microsecond=0)

                # Converte o prazo para datetime hoje (HH:MM)
                hora_prazo = datetime.strptime(prazo, "%H:%M").replace(
                    year=agora.year,
                    month=agora.month,
                    day=agora.day,
                    second=0,
                    microsecond=0
                )

                # Se o prazo for menor que agora, significa que passou da meia-noite → é do dia seguinte
                if hora_prazo < agora:
                    hora_prazo = hora_prazo.replace(day=hora_prazo.day + 1)

                # Diferença em minutos
                diferenca_minutos = (hora_prazo - agora).total_seconds() / 60

                # Atrasada
                if diferenca_minutos <= 0:
                    cor_texto = "red"
                    borda = "2px solid red"

                # Perto do prazo (até 60 min)
                elif diferenca_minutos <= 60:
                    cor_texto = "yellow"
                    borda = "2px solid yellow"

                # Longe do prazo (61+ min)
                else:
                    cor_texto = "white"
                    borda = "none"

            except:
                cor_texto = "white"
                borda = "none"

        else:
            # Sem prazo
            cor_texto = "green"
            borda = "2px solid green"

        # ----------------------------------------------------------

        # Se estiver concluída, fica verde
        if status == "Feito":
            cor_texto = "lightgreen"
            borda = "2px solid lightgreen"

        col1, col2 = st.columns([8, 1])

        with col1:
            st.markdown(
                f"""
                <div style="border:{borda}; padding:10px; border-radius:10px;">
                    <h3 style='color:{cor_texto}; margin:0;'>
                        {a+1} - {atividade} ({status})
                    </h3>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            if st.button("✅", key=f"btn_{a}"):
                marcar_como_feito(a)
                st.rerun()


# N A V E G A Ç Ã O
st.subheader("")
if st.button("Cadastrar novas atividades 📚"):
    st.switch_page("pages/Adicionar (menu).py")


# C O N T A D O R   D E   P E N D E N T E S

pendentes = [
    st.session_state.atividades[i]
    for i, status in enumerate(st.session_state.status_atividades)
    if status == "Pendente"
]

qtd_pendentes = len(pendentes)
total = len(st.session_state.status_atividades)

st.markdown(
    f"<h2 style='color:white;'>❌ Tarefas pendentes ❌: "
    f"<span style='color:black;'>{qtd_pendentes} / {total}</span></h2>",
    unsafe_allow_html=True
)

# L I S T A   D E   P E N D E N T E S

if pendentes:
    st.markdown("<h3 style='color:white;'>Lista de tarefas pendentes:</h3>", unsafe_allow_html=True)
    for item in pendentes:
        st.markdown(f"<h4>• {item}</h4>", unsafe_allow_html=True)
else:
    st.markdown("<h4 style='color:white;'>Nenhuma pendente! 🎉</h4>", unsafe_allow_html=True)


# Botão do "Sobre"

st.subheader("")
if st.button("Sobre"):
    st.switch_page("pages/Sobre.py")
