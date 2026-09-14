from langsmith import Client
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import time

from prompts import PLANNER_PROMPT, GENERATION_PROMPT


def format_docs(docs):
    """Retriever로 검색한 유사 문서의 내용을 하나의 string으로 결합"""
    return "\n\n".join(doc.page_content for doc in docs)


def get_prompt():
    client = Client()
    return client.pull_prompt(
        "rlm/rag-prompt",
        dangerously_pull_public_prompt=True
    )


def build_rag_chain(retriever, llm):
    """기존 RAG Chain"""
    prompt = get_prompt()

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
        | StrOutputParser()
    )

    print("Chain 선언 완료")
    return rag_chain


def build_planner_chain(llm):
    """사용자 요청을 분석해서 작업 계획을 만드는 Chain"""

    prompt = ChatPromptTemplate.from_template(PLANNER_PROMPT)

    planner_chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    print("Planner Chain 선언 완료")
    return planner_chain


def build_generation_chain(llm):
    """RAG 검색 결과를 바탕으로 최종 결과를 생성하는 Chain"""

    prompt = ChatPromptTemplate.from_template(GENERATION_PROMPT)

    generation_chain = (
        prompt
        | llm
        | StrOutputParser()
    )

    print("Generation Chain 선언 완료")
    return generation_chain


def stream_response(rag_chain, user_prompt: str):
    """기존 RAG 응답 스트리밍"""

    for chunk in rag_chain.stream(user_prompt):
        for char in chunk:
            print(char, end="", flush=True)
            time.sleep(0.03)

    print()