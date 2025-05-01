import requests
import streamlit as st

url1 = "http://localhost:8000/p1/invoke"
url2 = "http://localhost:8000/p2/invoke"

def get_mistral_response(input_text):
    response = requests.post(url= url1, json= {'input': {'topic': input_text}})
    return response.json()['output']['content']
def get_llama_response(input_text):
    response = requests.post(url= url2, json= {'input': {'topic': input_text}})
    return response.json()['output']['content']

st.title("langchain demo with LLamma 2 API")
input_text = st.text_input("provide the solution of given question")

if input_text:
    st.write(get_mistral_response(input_text))
    st.write(get_llama_response(input_text))
    
    

