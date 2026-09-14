from setup_env import ensure_packages
ensure_packages()

from dotenv import load_dotenv
import os
load_dotenv()

from loaders import load_all_pdfs
from splitter import split_pages
from embeddings import get_embeddings
from langchain_chroma import Chroma

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
NVIDIA_API_KEY = os.getenv("NVIDIA_BUILD_KEY")

pages = load_all_pdfs(GITHUB_TOKEN)
print(f"총 페이지: {len(pages)}")

docs = split_pages(
    pages,
    chunk_size=1000,
    chunk_overlap=100
)
print(f"총 청크: {len(docs)}")

embeddings = get_embeddings(NVIDIA_API_KEY)

vectorstore = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="./chroma_db"
)
print("Chroma DB 생성 완료")