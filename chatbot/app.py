from langchain.chat_models import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv('OPENROUTER_API_KEY')
#Langsmith Tracking
os.environ['LANGCHAIN_TRACING_V1'] = 'true'  #automatically tracing the code that we're gonna write
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

# Set up OpenRouter endpoint
openrouter_endpoint = "https://openrouter.ai/api/v1"

#Prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant. Please response to the user queries."),
        ("user", "Question: {question}")
    ]
)

#streamlit framework
st.title("Langchain Demo with Openrouter(Mistral)")
input_text = st.text_input("Search the topic you want")

#Mistral LLM
llm = ChatOpenAI(
    openai_api_base=openrouter_endpoint,
    model = "mistralai/mistral-7b-instruct",
    temperature = 0.7
)
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))
    
     