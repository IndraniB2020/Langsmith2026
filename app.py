

LANGCHAIN_API_KEY="lsv2_88*******************"
LANGCHAIN_PROJECT="Test 1"

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


import os
os.environ["LANGCHAIN_API_KEY"]=LANGCHAIN_API_KEY
os.environ["LANGCHAIN_PROJECT"]=LANGCHAIN_PROJECT
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
GROQ_API_KEY="gsk_*********************************"


prompt = PromptTemplate(
     input_variables=["Topics"],
     template="keep talking about {topic} in 10 lines"
)

llm = ChatGroq(
    api_key=GROQ_API_KEY,
    model="llama-3.3-70b-versatile",
    temperature=0.5,
    max_tokens=None
)

parser=StrOutputParser()

chain = prompt | llm | parser
print(chain.invoke({"topic":'Vikings'}))


