import streamlit as st
from src.chains.rag_chain import load_rag_chain
from src.utils.models import load_models

st.set_page_config(page_title="Medical Chatbot", page_icon="🧬")
st.markdown("""
    <style>
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif;
            background-color: #f0f2f6;
        }
        .stChatMessage {
            padding: 10px;
            border-radius: 10px;
        }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.title("🩺 Medical Diagnosis Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


if st.button("Reset Chat"):
    st.session_state.chat_history.clear()

if "rag_chain" not in st.session_state:
    with st.spinner("Loading models and chains"):
        print("Loading models")
        llm, retriever = load_models()
        print("Loading rag chain")
        st.session_state.rag_chain = load_rag_chain(llm, retriever)

query = st.chat_input("Ask a medical question:")

for chat in st.session_state.chat_history:
    with st.chat_message("user", avatar="👤"):
        st.markdown(chat["user"])
    with st.chat_message("ai", avatar="💬"):
        st.markdown(chat["ai"])

if query:
    with st.chat_message("user", avatar="👤"):
        st.markdown(query)
    
    with st.spinner("Thinking..."):
        response = st.session_state.rag_chain.invoke({"input": query})
        reply = response["answer"]
    
    with st.chat_message("ai", avatar="💬"):
        st.markdown(reply)
    
    st.session_state.chat_history.append({"user": query, "ai": reply})
