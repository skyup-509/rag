from langchain_nvidia_ai_endpoints import ChatNVIDIA

def get_llm(api_key: str, model: str = "google/diffusiongemma-26b-a4b-it"):
    return ChatNVIDIA(
        model=model,
        api_key=api_key,
        temperature=0,
        max_tokens=100
    )