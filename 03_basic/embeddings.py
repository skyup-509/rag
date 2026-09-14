from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

def get_embeddings(api_key: str, model: str = "nvidia/nemotron-3-embed-1b"):
    return NVIDIAEmbeddings(
        model=model,
        api_key=api_key
    )