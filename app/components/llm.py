from langchain_openai import ChatOpenAI
from app.config.config import KODEKLOUD_API_KEY, KODEKLOUD_BASE_URL
from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def load_llm(model_name: str = "x-ai/grok-3", api_key: str = KODEKLOUD_API_KEY):
    try:
        logger.info(f"Loading LLM from KodeKloud using {model_name} model...")

        llm = ChatOpenAI(
            api_key=api_key,
            base_url=KODEKLOUD_BASE_URL,
            model=model_name,
            temperature=0.3,
            max_tokens=256,
        )

        logger.info("LLM loaded successfully from KodeKloud.")
        return llm

    except Exception as e:
        error_message = CustomException("Failed to load an LLM from KodeKloud", e)
        logger.error(str(error_message))
        return None
