import streamlit as st
import os
import sys
# Add project root to sys.path BEFORE any imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..')))
import requests
from src.frontend_src.config.frontend_settings import Settings

settings = Settings()

st.set_page_config(
    page_title = "AstraRAG",
    page_icon = "🤖",
    layout = "centered"
)

st.title("💬 AstraRAG - Agentic RAG Chatbot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for msg in st.session_state.chat_history:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])
        if msg.get("role") == "assistant":
            sources = msg.get("sources",[])
            tool_used = msg.get("tool_used")
            rationale = msg.get("rationale")
            if sources:
                st.markdown(f"**Sources : **{', '.join (sources)}")
            if tool_used or rationale:
                with st.expander("Show details (tools and rationale)"):
                    st.markdown(f"**Tool used : **{tool_used if tool_used else 'N/A'}")
                    st.markdown(f"**Rationale : ** {rationale if rationale else 'N/A'}")

user_prompt = st.chat_input("Ask Chatbot ..")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role":"user","content":user_prompt})

    # Prepare payload for api
    payload = {"chat_history":st.session_state.chat_history}
    try:
        response  = requests.post(settings.CHAT_ENDPOINT_URL,json = payload)
        response.raise_for_status()
        response_json = response.json()
        assistant_response = response_json.get("answer","(No response)")
        tool_used = response_json.get("tool_used","N/A")
        sources = response_json.get("sources",[])
        rationale = response_json.get("rationale","N/A")
    except Exception as e:
        assistant_response= f"Error : {e}"
        tool_used = "N/A"
        rationale = "N/A"
        sources = []
    st.session_state.chat_history.append({
        "role":"assistant",
        "content" : assistant_response,
        "tool_used" : tool_used,
        "sources" : sources,
        "rationale" : rationale
    })

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
        if sources:
            st.markdown(f"**Sources : ** {' ,'.join(sources)}")
        with st.expander("Show details (tool and rationale)"):
            st.markdown(f"**Tool used : **{tool_used}")
            st.markdown(f"**Rationale : **{rationale}")
