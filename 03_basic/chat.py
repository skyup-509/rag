from dotenv import load_dotenv
import os
load_dotenv()

from embeddings import get_embeddings
from langchain_chroma import Chroma

from llm import get_llm
from chain import build_rag_chain, stream_response

NVIDIA_API_KEY = os.getenv("NVIDIA_BUILD_KEY")
embeddings = get_embeddings(NVIDIA_API_KEY)

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)
retriever = vectorstore.as_retriever()
print("Retriever 준비 완료")

llm = get_llm(NVIDIA_API_KEY)
rag_chain = build_rag_chain(retriever, llm)
print("RAG 준비 완료")

# Chatting 시작
print("질문을 입력하세요. 종료하려면 q를 입력하세요.")

while True:
    user_prompt = input("\n질문: ")
    if user_prompt.lower() == 'q':
        break

    stream_response(rag_chain, user_prompt)