import os
from dotenv import load_dotenv
load_dotenv()

# 파일 불러오는 url 설정
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

GITHUB_OWNER = "skyup-509"
GITHUB_REPO = "data-store"
GITHUB_PATH = "pdf_data"
GITHUB_REF = None

def get_github_api_url():
    url = f"https://api.github.com/repos/{GITHUB_OWNER}/{GITHUB_REPO}/contents/{GITHUB_PATH}"
    if GITHUB_REF:
        url += f"?ref={GITHUB_REF}"
    return url
