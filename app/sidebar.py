import streamlit as st

def setup_sidebar(chat_placeholder):
    """
    Sets up the sidebar for the Streamlit app.

    - Provides options to upload documents, process them, and start a new chat session.
    - Initializes the conversation chain after processing the documents.

    Args:
        chat_placeholder: A Streamlit placeholder for displaying messages in the chat interface.
    """
    with st.sidebar:
        if st.button("Start New Chat"):
            st.session_state.chat_history = []
            st.session_state.chat_history.append({"role": "system", "content": "Hello! I am Shash LLM. How can I help you today 🤖?"})
            st.success("New chat started! Please upload a document to begin.")
            chat_placeholder.empty()
        
        st.markdown("---")
        # Display user queries from the chat history
       
        user_queries = [message['content'] for message in st.session_state.chat_history if message['role'] == 'user']
        if user_queries and len(user_queries) > 0: 
            st.write("User Queries:")
            for query in user_queries:
                st.write(f"- {query}")
        else:
            st.write("No user queries yet.")


        

        
