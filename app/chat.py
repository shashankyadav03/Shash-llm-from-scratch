import streamlit as st
import logging
from app.display import display_chat_history
from services.inference import run_inference

base_prompt = """
The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.You are Shash, a consult of AI Integrations"""

def parse_chat_history(chat_history):
    """
    Parses the chat history to display the conversation in a readable format.

    Args:
        chat_history (list): The chat history containing user and system messages.

    Returns:
        str: The parsed chat history as a string.
    """
    parsed_history = ""
    for message in chat_history:
        role = "User" if message['role'] == "user" else "System"
        parsed_history += f"{role}: {message['content']}\n"
    return parsed_history

def handle_user_query(user_query):
    """
    Handles the user query and generates a response using the conversation chain.

    - Checks if the conversation chain is initialized.
    - Sends the user query to the conversation chain and retrieves the response.
    - Handles cases where the LLM is uncertain or provides an insufficient response.
    - Updates and displays the chat history.
    
    Args:
        user_query (str): The user's input/query.
    """

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    try:
        parsed_history = parse_chat_history(st.session_state.chat_history)
        new_prompt = f"Focus on current prompt: {user_query}\n The chat history is as follows just take this as context: {parsed_history}"
        if not parsed_history or len(parsed_history) < 10:
            system_message = run_inference(user_query, base_prompt)
        else:
            system_message = run_inference(new_prompt, base_prompt)

        # Update the chat history with user query and system response
        st.session_state.chat_history.append({"role": "user", "content": user_query})
        st.session_state.chat_history.append({"role": "system", "content": system_message})

        # Display the chat history
        display_chat_history()

    except KeyError as ke:
        logging.error(f"KeyError: Missing expected key - {ke}")
        st.error(f"A system error occurred: {ke}. Please try again.")
    except Exception as e:
        logging.exception("An unexpected error occurred")
        st.error(f"An error occurred while processing your query: {e}")
