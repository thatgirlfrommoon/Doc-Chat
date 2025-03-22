#                                    ✨  Doc-Chat ✨

[![GitHub stars](https://img.shields.io/github/stars/thatgirlfrommoon/Doc-Chat?style=social)](https://github.com/thatgirlfrommoon/Doc-Chat/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/thatgirlfrommoon/Doc-Chat?style=social)](https://github.com/thatgirlfrommoon/Doc-Chat/forks)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-yellow.svg)](https://opensource.org/license/apache-2-0)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1yrS2Kp-kprYWot_sEu7JeWMIRAei_vov?usp=sharing)
[![LangChain](https://img.shields.io/badge/LangChain-Open%20SourceFramework-5e9cff?logo=langchain&logoColor=white)](https://python.langchain.com/docs/introduction/)
[![Streamlit UI](https://static.streamlit.io/badges/streamlit_badge_black_red.svg)](https://streamlit.io/)



Doc-Chat is a repository for you to chat and extract insights from any website or document of your choice.

Possible Use Cases:
- ⚡ A web documentation that you are curious about.
- 📫 A pdf book online.
- ⚡ A recently released publication

If it's accessible to crawl, it's yours! The Doc-chat is ready to absorb any knowledge you provide and will serve as your trusty study companion!

# What is Doc-Chat?

![alt text](./images/workflow.png)


##  Get started

1. **Clone the repository**

    - ``` bash
        https://github.com/thatgirlfrommoon/Doc-Chat.git 
        ```

    Or start a codespace from the repository.
    - ```bash
      https://codespaces.new/thatgirlfrommoon/Doc-Chat
      ```
2. **Install uv**

    MacOS/Linux:

    - ```bash
      curl -LsSf https://astral.sh/uv/install.sh | s
      ```

        
    Windows:

    - ```bash 
      powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"```
      
Make sure to restart your terminal afterwards to ensure that the uv command gets picked up.
    
3. **Install Dependencies** 📦
    ```bash
    uv sync
    ```

4. **Set up OPENAI key**
Add the key in ".env-sample" files in two paths paths 
   - main folder
   - ".\VectorDB\env-sample"

    and rename both files to ".env".

5. **Now start crawling.**

Enter a valid url to crawl and wait for few seconds to process. Try:

- https://huggingface.co/docs/transformers/en/index

With this, the crawled document would be available in the main directory "./scraped_files" as text files. 

6. **vector DB Storage**

    Once the text files are saved locally, we store the embedded data of the same in a vectorDB persisted at:

- ```bash
  .\VectorDB\create_vector_store.py
    ```

With this step chromadb collections are created in ```./vectorstore``` path.

7. **Power up the bot**

- ```bash
  uv run streamlit run app.py
  ```


A link will open up in the browser with url : http://localhost:8501/ (or similar)

There you go!
