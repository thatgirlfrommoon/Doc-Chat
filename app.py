import streamlit as st
import DocChat_backend

# create a Gradio interface
def create_streamlit_interface():

    st.title("RAG based Conversational AI bot")

    # Display the chat message
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    st.sidebar.title("Model parameters")

    if prompt := st.text_input("Hi👋, What's up🧑‍💻?"):
        st.session_state.messages.append({"role": "user",
                                           "content": prompt})
        # display the user message
        with st.chat_message("user"):
            st.markdown(prompt)

        # Display the bot response
        with st.chat_message("assistant"):
            # Simulate the stream of responses with milliseconds delay
            
            message_placeholder = st.empty()
            # full_response = ""
            full_response = DocChat_backend.chat_with_bot(user_input=prompt,
                                                                       conversation_history= st.session_state.messages)
            
            # # Add blinking cursor to simulate typing
            message_placeholder.markdown(full_response)
            
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    

if __name__ == "__main__":
    create_streamlit_interface()