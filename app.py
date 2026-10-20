import streamlit as st
from tutor import obter_resposta_tutor

st.set_page_config(page_title="Tutor Minimalista", page_icon="🎓")

st.markdown("<style>main {background-color: #0f172a; color: white;}</style>", unsafe_allow_html=True)

st.title("Tutor IA Otimizado")
st.caption("Focado em Português e Matemática | Alta Performance")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    role = "user" if message.role == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(message.parts[0].text)

if prompt := st.chat_input("Como posso te ajudar hoje?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("Analisando..."):
            resposta, novo_historico = obter_resposta_tutor(
                st.session_state.chat_history, 
                prompt
            )
            st.markdown(resposta)
    
    st.session_state.chat_history = novo_historico