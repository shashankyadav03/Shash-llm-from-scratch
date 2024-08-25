import streamlit as st
from services.dotenv_loader import load_environment
from app.sidebar import setup_sidebar
from app.chat import handle_user_query

def main():
    """
    Main function to run the Streamlit app.
    
    - Sets up the environment variables.
    - Initializes session state variables.
    - Sets up the Streamlit page configuration.
    - Handles user interactions via the chat interface and sidebar.
    """
    load_environment()

    # Set up Streamlit page configurations
    st.set_page_config(page_title="Shash LLM", page_icon="🤖")

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Header and Subheader for the application
    st.header("Shash LLM 🤖")
    st.subheader("LLM build from scratch")

    # Placeholder for the chat interface
    chat_placeholder = st.empty()

    # Setup the sidebar for document upload and processing
    setup_sidebar(chat_placeholder)

    # Handle user input through the text input box
    user_query = st.text_input("Chat with the custom llm below:")
    if user_query:
        handle_user_query(user_query)

if __name__ == '__main__':
    main()
