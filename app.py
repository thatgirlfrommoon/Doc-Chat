import streamlit as st
import DocChat_backend
from crawling_pipeline import pipeline
import time

st.set_page_config(page_title="Doc-Chat", page_icon="🤖", layout="wide") 

# create a Gradio interface
def create_streamlit_interface():

    st.title("Welcome to Doc-Chat🤖 !")
    st.snow()

    user_url = st.text_input("Enter URL to Crawl")
    

    if user_url:
        if st.button("Strart Crawling"):
            with st.spinner("Wait for it...", show_time=True):
                crawl_status = pipeline(url=user_url)
                if crawl_status==2:
                    st.success("Read the website!")
                else:
                    st.success("Already added!")
    
            
    # if crawl_status:
    #     print("Hi")
    #     st.markdown("Sucess!")
    # else:
    #     st.markdown("Failed to add the url to database")


    # Display the chat message
    if 'messages' not in st.session_state:
        st.session_state.messages = []
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    st.sidebar.header("Model parameter")
    st.sidebar.write("Customize the chatbot’s behavior by adjusting the settings below.")
    temp = st.sidebar.slider("Temperature", 0.0, 1.0, 0.1, key="temperature")
    max_tokens = st.sidebar.slider("Max tokens", 50, 500, 150, key="max_tokens")

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
                                                          args={"temperature": temp, "max_tokens": max_tokens},
                                                          conversation_history= st.session_state.messages,
                                                          url = user_url)
            
            # # Add blinking cursor to simulate typing
            message_placeholder.markdown(full_response)
            
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": full_response})
    

if __name__ == "__main__":
    create_streamlit_interface()