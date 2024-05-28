
# Data in Health AI Course

## LangChain RAG Based Chatbot Example
In this example, we develp a Chatbot which incorporates custom documents to provide up to date answers based on those documents.

## Project Setup 
The repository contains the following key directories.
> **data.** This folder contains the documents which need the Chatbot to use
> 
> **store.** The Chroma vector database files are stored in this directory
> 
> **examples.**. This folder contains example documents which can be used in case the data folder doesnt have any

Note that this an advanced version of what we covered in the LangChain tutorial. All the different components of creating Chatbot such as creating chains, memory management, loading and splitting documents is handled in seperate Pythin modules (files). Although this looks complicated, its the best practice for deploying Python apps in the wild. 

The following Python scripts are the important ones to understand. Feel free to read and explore what the other scripts are doing.
>**streamlit_app.py** This is the Streamlit app script
>
>**local_loader.py** This script has LangChain functions which are loading the PDF files and get them ready for storage in vector database.
>
>**full\_chain.py/basic\_chain.py** These too files contains the LangChain prompts logic. 


## Python Setup

### Setup Python virtual environment

The Python version used when this was developed was 3.10.13


```bash
python -mvenv .venv
source .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

If you run into issues related to hnswlib or chroma-hnswlib while installing requirements you may need to install system package for the underlying package.

For example, on Ubuntu 22.04 this was needed before pip install of hnswlib would succeed.

```bash
sudo apt install python3-hnswlib
```

### Setup .env file with API tokens needed.

```
OPENAI_API_KEY="<Put your token here>"
HUGGINGFACEHUB_API_TOKEN="<Put your token here>"
```

### Setup Streamlit app secrets.

#### 1. Set up the .streamlit directory and secrets file.

```bash
mkdir .streamlit
touch .streamlit/secrets.toml
chmod 0600 .streamlit/secrets.toml
```

#### 2. Edit secrets.toml

**Either edit `secrets.toml` in you favorite editor.**

```toml
OPENAI_API_KEY="<Put your token here>"
HUGGINGFACEHUB_API_TOKEN="<Put your token here>"
```

**Or, you can just reuse .env contents from above.**

```bash
cat < .env >> .streamlit/secrets.toml
```

### Verify Environment

1. Check that LangChain dependencies are working.

```bash
python basic_chain.py
```

2. Check that Streamlit and dependencies are working.
The output you will see is from an example document (a book by Bertrand Russel) just to check that the script is working.

```bash
streamlit run streamlit_app.py
```

>    Split into 313 chunks
>    According to Russell, the key problems of philosophy include the uncertainty of knowledge, the limitations of metaphysical reasoning, and the inability to provide definite answers to fundamental questions. Philosophy aims to diminish the risk of error, but cannot eliminate it entirely due to human fallibility. The value of philosophy lies in its ability to challenge common sense beliefs and lead to the exploration of complex problems.



## Example Queries for the Chatbot
The Chatbot will answer questions on health outbreaks as announced by WHO

### Question 1: Check whether there is an outbreak in a country
**Question:** Is there a disease outbreak in Zambia?

**Answer:**
Yes, there is currently an outbreak of anthrax in Zambia, particularly in the Sinazongwe district, which is the epicenter of the outbreak. The outbreak has spread to several provinces in the country, affecting both animals and humans.

**Question:** What about Tunisia?

**Answer:**
I don't have information about a current disease outbreak in Tunisia. If you have any specific concerns or need more details, I recommend checking the latest updates from official health sources or the World Health Organization for the most accurate information.

### Example 2: Details about a disease outbreak

**Question:**
When did anthrax start in Zambia?

**Answer:**
The anthrax outbreak in Zambia began on 1 November 2023 when the IHR National Focal Point of Zambia notified WHO of the outbreak in humans.

**Question:**
Has anyone died due to anthrax in Zambia?

**Answer:**
Yes, there have been sporadic suspected cases and deaths reported in different districts and provinces of Zambia since June 2023 due to the anthrax outbreak. The epidemic is spreading along the provinces located along specific rivers, and the Bacillus anthracis bacteria can form highly resistant spores that survive in the environment for decades. The risk for human fatalities is present, especially in cases of severe illness that can lead to respiratory failure and other complications.


## References
This app was adapted from the [Streamlit example app](https://github.com/streamlit/example-app-langchain-rag).


## Misc Notes

- There is an issue with newer langchain package versions and streamlit chat history, see https://github.com/langchain-ai/langchain/pull/18834
  - This one reason why a number of dependencies are pinned to specific values.
