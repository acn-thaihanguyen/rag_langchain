from typing import Set

import streamlit as st
from streamlit_chat import message

from src.retriever import run_llm


def create_sources_string(source_urls: Set[str]) -> str:
    """
    Creates a formatted string of source URLs.

    Args:
        source_urls (Set[str]): A set of source URLs.

    Returns:
        str: A formatted string listing all source URLs.
    """
    if not source_urls:
        return ""
    sorted_sources = sorted(source_urls)
    sources_string = "\nSources:\n "
    for idx, source in enumerate(sorted_sources, start=1):
        sources_string += f"Paper: {idx}. {source}\n"
    return sources_string

def initialize_session_state():
    """
    Initializes session state variables for chat history if they do not exist.
    """
    if "chat_answers_history" not in st.session_state:
        st.session_state["chat_answers_history"] = []
    if "user_prompt_history" not in st.session_state:
        st.session_state["user_prompt_history"] = []
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

def display_chat_history():
    """
    Displays the chat history in the Streamlit app.
    """
    if st.session_state["chat_answers_history"]:
        for user_query, generated_response in zip(
            st.session_state["user_prompt_history"],
            st.session_state["chat_answers_history"]
        ):
            message(user_query, is_user=True)
            message(generated_response)

def main():
    """
    Main function to run the Streamlit app.
    Sets up the page configuration, initializes session state,
    handles user input, and displays chat history.
    """
    st.set_page_config(
        page_title="Smart Document Query System",
        page_icon=":mag:",
        layout="wide",
        initial_sidebar_state="auto"
    )
    
    with st.sidebar:
        st.image("./icons/chatbot.png", width=100)
        st.markdown("## Smart Document Query System")
        st.markdown("Effortlessly search and retrieve information from your documents using our advanced RAG system.")
        st.markdown("---")
        st.markdown("[Open in GitHub](https://github.com/acn-thaihanguyen/rag_langchain)")
        st.markdown("[Author: Nguyen Thai Ha]")
    
    st.title("Smart Document Query System")
    st.caption("🔍 Seamlessly integrated with LangChain for precise document queries.")

    initialize_session_state()

    prompt = st.text_input("Enter your question:", placeholder="Type your query here...")

    if prompt:
        with st.spinner("Searching for the answer..."):
            response = run_llm(prompt)
            sources = {doc.metadata["source"] for doc in response["source_documents"]}
            formatted_response = f"{response['answer']} \n {create_sources_string(sources)}"
            
            st.session_state.chat_history.append((prompt, response["answer"]))
            st.session_state.user_prompt_history.append(prompt)
            st.session_state.chat_answers_history.append(formatted_response)

    display_chat_history()

if __name__ == "__main__":
    main()
