# CHATBOT-USING-PYTHON
AI-powered chatbot web app. built using Streamlit Lang,Chain with the Groq LLM (LLaMA 3.1) model.The application maintains chat history using Streamlit’s session state, enabling contextual conversations instead of single-turn responses. It is lightweight, fast and easy to extend with more features such as memory, file uploads, or API integrations
## 🚀 Features

- 💬 Interactive chat interface
- 🧠 Context-aware conversation (chat history)
- ⚡ Fast responses using Groq LLM
- 🌐 Web-based UI with Streamlit
- 🛠 Simple and beginner-friendly code structure
## 🧰 Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **Groq LLM (llama-3.1-8b-instant)**
## Installation & Run Steps

## Step 1: Install Python
Make sure Python 3.9 or above is installed on your system.
Check version using:
python --version

## Step 2: Create Project Folder
Create a new folder and move your app.py file into it.

## Step 3: Install Required Dependencies
Install Streamlit:
python -m pip install streamlit

Install LangChain and Groq:
python -m pip install langchain langchain-groq

## Step 4: Set Groq API Key

For Windows (CMD / PowerShell):
setx GROQ_API_KEY "your_api_key_here"



## Step 5: Run the Application
Run the following command inside the project folder:
python -m streamlit run app.py

## Step 6: Open in Browser
The app will open automatically in your browser.
If not, open manually at:
http://localhost:8501
