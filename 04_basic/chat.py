from dotenv import load_dotenv
import os

load_dotenv()

from embeddings import get_embeddings
from langchain_chroma import Chroma

from llm import get_llm
from chain import build_rag_chain
from planner import make_plan
from utils import get_files, save_file


NVIDIA_API_KEY = os.getenv("NVIDIA_BUILD_KEY")

OUT_DIR = "./out"


# Embedding
embeddings = get_embeddings(NVIDIA_API_KEY)

# Vector DB
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever()

# LLM
llm = get_llm(NVIDIA_API_KEY)


print("RAG 준비 완료")
print("질문을 입력하세요. 종료하려면 q를 입력하세요.")


while True:
    user_request = input("\n질문: ")

    if user_request.lower() == "q":
        break

    files = get_files(OUT_DIR)

    plan = make_plan(
        llm=llm,
        user_request=user_request,
        out_dir=OUT_DIR,
        files=files
    )

    print("\n[작업 계획]")
    print(plan)

    # TODO:
    # plan의 search_query를 이용해 RAG 검색
    # 필요한 함수를 실행
    # 최종 결과 생성
    # out_dir에 저장