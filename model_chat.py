# -*- coding: utf-8 -*-
"""Model_chat.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AiXkCKhxKNMf4LQoKa1lzBj63FizCP8F
"""

!pip install langchain

!pip install langchain_community

from langchain import HuggingFaceHub
from langchain import PromptTemplate, LLMChain

# Set up the Falcon-40B-Instruct model
repo_id = "tiiuae/falcon-7b-instruct"
huggingfacehub_api_token = "----------------------"  # Replace with your Hugging Face API token

# Initialize HuggingFaceHub with the provided API token and repo ID
llm = HuggingFaceHub(
    huggingfacehub_api_token=huggingfacehub_api_token,
    repo_id=repo_id,
    model_kwargs={"temperature": 0.7, "max_new_tokens": 500}
)

from re import template
template = """Question: {question}

Answer: Let's give a detailed answer."""

# Set up the PromptTemplate and LLMChain
prompt = PromptTemplate(template=template, input_variables=["question"])
chain = LLMChain(prompt=prompt, llm=llm)

# Function to get answer from model
def get_answer(question):
    out = chain.run(question=question)
    return out

# Accept user input for the question
user_question = input("Please enter your question: ")

# Get the answer for the user's question
answer = get_answer(user_question)

# Display the answer
print("Answer:", answer)