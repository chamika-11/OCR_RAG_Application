import os
from langchain_community.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document
from env_loader import *

def ask_question(text,question):
    docs=[Document(page_content=text)]

    llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo-instruct")
    chain = load_qa_chain(llm, chain_type="stuff")

    result=chain.run(input_documents=docs,question=question)
    return result
    