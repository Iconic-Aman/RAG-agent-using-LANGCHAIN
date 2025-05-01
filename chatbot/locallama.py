from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
#Langsmith Tracking
os.environ['LANGCHAIN_TRACING_V1'] = 'true'  #automatically tracing the code that we're gonna write
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')


#Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant. Please response to the user queries."),
        ("user", "Question: {question}")
    ]
)

#streamlit framework
st.title("Langchain Demo with Ollama(LLama 2)")
input_text = st.text_input("Search the topic you want")

#Mistral LLM
llm = Ollama(
    model = "llama2-uncensored",
    temperature = 0.7
)
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
