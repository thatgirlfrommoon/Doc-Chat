#                                    ✨  Doc-Chat ✨  
[![GitHub stars](https://img.shields.io/github/stars/thatgirlfrommoon/Doc-Chat?style=social)](https://github.com/thatgirlfrommoon/Doc-Chat/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/thatgirlfrommoon/Doc-Chat?style=social)](https://github.com/thatgirlfrommoon/Doc-Chat/forks)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://opensource.org/license/apache-2-0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yrS2Kp-kprYWot_sEu7JeWMIRAei_vov?usp=sharing)
[![Streamlit](https://img.shields.io/badge/UI%20_-Streamlit_-00bda?style=flat-square)](https://streamlit.io/)
[![LangChain](https://img.shields.io/badge/LangChain-Open%20SourceFramework-5e9cff?logo=langchain&logoColor=white)](https://python.langchain.com/docs/introduction/)
[![ChromaDB](https://img.shields.io/badge/Chroma%20AI-Vector--DB_-00bda?style=flat-square)](https://www.trychroma.com/) 

Doc chat is learning repository for you to chat with a document of your choice and extract insights from it.

The document could be
- ⚡ A web documentation that youa are curious about
- 📫 A pdf book online
- ⚡ A publication that just released

If it is available to crawl, you have it ! The Doc-chat is ready to consume any knowledge that you present and would act as your study buddy!


# Setup
- $ Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser


# Python package
- $ uv init 
- $ uv run .\hello.py


# Install packages
- $ uv pip install -r requirements.txt

# Power up the bot
Set up the OpenAI API key in code before running it
- $ uv run streamlit run .\bot\bot_ui2.py
