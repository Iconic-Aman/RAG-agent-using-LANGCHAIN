from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes

import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv
load_dotenv ()

os.environ['OPENAI_API_KEY'] = os.getenv('OPENROUTER_API_KEY')
#Langsmith Tracking
os.environ['LANGCHAIN_TRACING_V1'] = 'true'  #automatically tracing the code that we're gonna write
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')

# Set up OpenRouter endpoint
openrouter_endpoint = "https://openrouter.ai/api/v1"

app = FastAPI(
    title= "Langchain Server",
    version= '1.0',
    description= "A simple API server"
)

add_routes(
    app,
    ChatOpenAI(),   
    path = '/openai'
)

model = ChatOpenAI(
    openai_api_base=openrouter_endpoint,
    model = "mistralai/mistral-7b-instruct",
    temperature = 0.7
)

#Ollama (LLama)
llm = Ollama(
    model = "llama2-uncensored",
    temperature = 0.7
)

prompt1 = ChatPromptTemplate.from_template("Write a python code in oops to create library management system")
prompt2 = ChatPromptTemplate.from_template("Write a python code in oops to create library management system")

add_routes(
    app,
    prompt1|model,
    path = "/p1"
)

add_routes(
    app,
    prompt2|llm,    
    path = "/p2"
)

if __name__ == "__main__":
    uvicorn.run(app, host= 'localhost', port= 8000)



