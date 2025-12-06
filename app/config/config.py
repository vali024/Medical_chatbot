import os
HF_TOKEN = os.environ.get("HF_TOKEN")
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
KODEKLOUD_API_KEY = os.environ.get("KODEKLOUD_API_KEY", "Sk-kkAI-ae19c61ea5ff308bdd4881f07f4a8e47c62639ea28aa7abc6eca503554ceab4dkk_91176949-83d3-428c-9de8-d4436b1b5792-kk290872e5")
KODEKLOUD_BASE_URL = "https://kodekey.ai.kodekloud.com/v1"

HUGGINGFACE_REPO_ID="mistralai/Mistral-7B-Instruct-v0.3"
DB_FAISS_PATH="vectorstore/db_faiss"
DATA_PATH="data/"
CHUNK_SIZE=500
CHUNK_OVERLAP=50
