from langsmith import Client
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
import time

def format_docs(docs):
    """Retriever로 검색한 유사 문서의 내용을 하나의 string으로 결합"""
    return "\n\n".join(doc.page_content for doc in docs)

def get_prompt():
    client = Client()
    return client.pull_prompt("rlm/rag-prompt", dangerously_pull_public_prompt=True)

def build_rag_chain(retriever, llm):
    prompt = get_prompt()
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )
    print("Chain 선언 완료")
    return rag_chain

def stream_response(rag_chain, user_prompt: str):
    for chunk in rag_chain.stream(user_prompt):
      for char in chunk:
        print(char, end="", flush=True)
        time.sleep(0.03)
    print()  # 스트리밍 끝나고 줄바꿈