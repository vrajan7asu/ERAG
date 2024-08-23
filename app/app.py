import streamlit as st
from streamlit_chat import message
import os

def main():
    st.set_page_config(page_title="ERAG", layout="wide")

    # Sidebar
    with st.sidebar:
        st.title("Configuration")
        
        # Radio buttons
        option = st.radio("Choose an option:", ("URL", "Document"))
        
        # File uploader
        uploaded_file = st.file_uploader("Upload a document", type=["txt", "pdf", "docx"])
        
        if uploaded_file is not None:
            st.success(f"File '{uploaded_file.name}' uploaded successfully!")
        
        # Dropdown for model selection
        model = st.selectbox("Select a model:", ("Model 1", "Model 2", "Model 3"))

    # Main chat interface
    st.title("ERAG: Enhanced Document Querying")

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("What is your question?"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"Echo: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()