from pathlib import Path
import os
from dotenv import load_dotenv

# Теперь BASE_DIR — это корень TUSUR_Project (/content/TUSUR_Project)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
dotenv_path = os.path.join(BASE_DIR, '.env')

# Загружаем .env из корня проекта
load_dotenv(dotenv_path=dotenv_path)

# Папка, где лежит constants.py (теперь это корень TUSUR_Project)
CURRENT_DIR = Path(__file__).parent

# ИСПРАВЛЕНО: Так как constants.py уже в корне, .parent больше не нужен!
# Папка data будет создаваться прямо в /content/TUSUR_Project/data/
CHROMA_PATH = CURRENT_DIR / "data" / "vector_store"
CHROMA_PATH.mkdir(parents=True, exist_ok=True)
CHROMA_PATH = str(CHROMA_PATH)

CHROMA_COLLECTION = "embeddings"
EMBEDDINGS_MODEL = "snowflake-arctic-embed2:latest"

# ИСПРАВЛЕНО: Убран .parent, база SQLite будет в корневой папке data
DB_PATH = CURRENT_DIR / "data" / "db_file" / "record_manager_cache.sql"
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
RECORD_MANAGER = f"sqlite+aiosqlite:///{DB_PATH.as_posix()}"

LLM_MODEL = "qwen2.5:14b-instruct-q4_K_M"

MAX_CONTEXT_CHARS = 40000
MAX_INPUT_CHARS = 20000

POSTGRES_USER = os.getenv("POSTGRES_USER", "analyst")
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD', '12345678')
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = os.getenv("POSTGRES_PORT", "5432")
POSTGRES_DB = os.getenv("POSTGRES_DB", "bpmn_models")

POSTGRES_CONNECTION_ASYNC_URL = f"postgresql+asyncpg://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
POSTGRES_CONNECTION_SYNC_URL = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
