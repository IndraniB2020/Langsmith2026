
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os

# Load .env file
load_dotenv()

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Tell me about {topic} in 20 lines"
)

llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model="openai/gpt-oss-120b",
    temperature=0.0,
    max_tokens=None
)

parser = StrOutputParser()

chain = prompt | llm | parser


response = chain.invoke({"topic": "History of Zeros"})

if hasattr(response, 'content'):
    print(response.content)
else:
    print(response)