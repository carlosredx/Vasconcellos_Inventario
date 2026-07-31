import os
from pathlib import Path

# Intentar cargar variables desde .env si python-dotenv está disponible
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parent.parent / '.env'
    load_dotenv(dotenv_path=env_path)
except ImportError:
    pass

class Config:
    """Configuración centralizada de la aplicación y la base de datos."""
    SECRET_KEY = os.getenv("SECRET_KEY", "vasconcellos-inventario-secret-key")
    DEBUG = os.getenv("FLASK_DEBUG", "True").lower() in ("true", "1", "t")
    PORT = int(os.getenv("PORT", 5000))
    
    # Motor de base de datos ('sqlite' o 'postgresql')
    DB_ENGINE = os.getenv("DB_ENGINE", "sqlite").lower()
    
    # Configuración SQLite
    SQLITE_DB_PATH = Path(__file__).resolve().parent.parent / os.getenv("SQLITE_DB_PATH", "database.db")
    
    # Configuración PostgreSQL
    # URL completa (ej. postgresql://user:password@host:port/dbname)
    DATABASE_URL = os.getenv("DATABASE_URL", "")
