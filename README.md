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

# Brain of Doc-Chat

![alt text](./images/workflow.png)

# How to use Doc-Chat
- Clone the repository :
    - ```git clone https://github.com/thatgirlfrommoon/Doc-Chat.git```
- Run app.py
    - ```streamlit run app.py```


# Development Setup

For Windows: 
Install uv for python package management from https://docs.astral.sh/uv/getting-started/installation/

- ```curl -LsSf https://astral.sh/uv/install.sh | less```
or 
- ```pip install uv```


# Python package
The pyproject.toml contains metadata about the project. The following command will create a pyproject.toml file.
- ```uv init```

To create a virtual environment at .venv
- ```uv venv```

The virtual environment can be "activated" to make its packages available

In Terminal
- ```source .venv/bin/activate```

In powershell
- ```.venv\Scripts\activate```

# Install packages
uv.lock is a human-readable TOML file but is managed by uv and should not be edited manually.
- ```uv run .\hello.py```


# Set up OPENAI key
Add the key in ".env-sample" file in the path "./bot" and rename the file name to ".env".

# Run the Crawler
- ```cd .\DocCrawl\```

Now start crawling (You may edit the urls to crawl, if needed) 
- ```scrapy crawl document_spider```

With this, the crawled document would be available in the main directory "./scraped_files" as text files.
For the time being, we consider only one scraped file for next step.

# Create a vector DB Storage
- ```cd ..```
- ```uv run .\VectorDB\create_vector_store.py```

With this step, based on the length of the document, chromadb collections are created in "./vectorstore" path.


# Power up the bot
- ```streamlit run app.py```


A link will open up in the browser with url : http://localhost:8501/ 

There you go!
