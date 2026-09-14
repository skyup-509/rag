import importlib
import subprocess
import sys

REQUIRED_PACKAGES = {
    "langchain": "langchain",
    "langchain_community": "langchain-community",
    "langchain_openai": "langchain-openai",
    "langchain_chroma": "langchain-chroma",
    "langchain_text_splitters": "langchain-text-splitters",
    "pypdf": "pypdf",
    "langchain_nvidia_ai_endpoints": "langchain_nvidia_ai_endpoints",
    "langchainhub": "langchainhub",
}

def ensure_packages(packages: dict = REQUIRED_PACKAGES):
    for module_name, pip_name in packages.items():
        try:
            importlib.import_module(module_name)
        except ImportError:
            print(f"설치 중: {pip_name}")
            subprocess.run([sys.executable, "-m", "pip", "install", "-U", pip_name], check=True)
    print("모든 패키지 준비 완료")