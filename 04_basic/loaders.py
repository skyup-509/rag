import requests
from concurrent.futures import ThreadPoolExecutor
from langchain_community.document_loaders import PyPDFLoader
from config import get_github_api_url

def fetch_pdf_files(github_token: str):
    headers = {
        "Authorization": f"Bearer {github_token}",
        "Accept": "application/vnd.github+json"
    }
    response = requests.get(get_github_api_url(), headers=headers)
    files = response.json()
    return [f for f in files if f["name"].lower().endswith(".pdf")]

def load_pdf(file):
    print("처리 중...")
    print(file["name"])
    loader = PyPDFLoader(file["download_url"])
    pdf_pages = loader.load_and_split()
    for page in pdf_pages:
        page.metadata["source_file"] = file["name"]
    return pdf_pages

def load_all_pdfs(github_token: str, max_workers: int = 5):
    pdf_files = fetch_pdf_files(github_token)
    pages = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = executor.map(load_pdf, pdf_files)
        for result in results:
            pages.extend(result)
    return pages