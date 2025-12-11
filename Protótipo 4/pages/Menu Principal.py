import streamlit as st
from datetime import datetime

# I N I C I A L I Z A Ç Ã O
if "atividades" not in st.session_state:
    st.session_state.atividades = []

if "status_atividades" not in st.session_state:
    st.session_state.status_atividades = []

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

# P R A Z O
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
    for idx, (atividade, status) in enumerate(zip(st.session_state.atividades, st.session_state.status_atividades)):
        prazo = extrair_prazo(atividade)

        # Cor padrão
        cor_texto = "white"
        borda = "none"

        # LÓGICA DO PRAZO SEGURA
        if prazo:
            try:
                h, m = map(int, prazo.split(":"))
                if not (0 <= h <= 23 and 0 <= m <= 59):
                    raise ValueError("Hora inválida")

                agora = datetime.now()
                agora_minutos = agora.hour * 60 + agora.minute
                prazo_minutos = h * 60 + m
                diferenca_minutos = prazo_minutos - agora_minutos

                if diferenca_minutos <= 0:
                    cor_texto = "red"
                    borda = "2px solid red"
                elif diferenca_minutos <= 60:
                    cor_texto = "yellow"
                    borda = "2px solid yellow"
                else:
                    cor_texto = "white"
                    borda = "none"

            except:
                # Prazo inválido → mantém padrão
                cor_texto = "white"
                borda = "none"
        else:
            # Sem prazo → cor neutra
            cor_texto = "white"
            borda = "none"

        # Se estiver concluída, fica verde
        if status == "Feito":
            cor_texto = "lightgreen"
            borda = "2px solid lightgreen"

        # Exibição
        st.markdown(
            f"""
            <div style="border:{borda}; padding:10px; border-radius:10px; margin-bottom:5px;">
                <h3 style='color:{cor_texto}; margin:0;'>
                    {idx+1} - {atividade} ({status})
                </h3>
            </div>
            """,
            unsafe_allow_html=True
        )
        with col2:
            if st.button("✅", key=f"btn_{a}"):
                marcar_como_feito(a)
                st.experimental_rerun()

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


