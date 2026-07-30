import sys
from pathlib import Path

# Agregar raíz al PYTHONPATH
root_dir = Path(__file__).resolve().parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from backend.app import create_app
from backend.app.config import Config
from backend.database_schema.init_db import init_db

app = create_app(Config)

if __name__ == "__main__":
    try:
        init_db()
    except Exception as e:
        print(f"[!] Advertencia al inicializar la base de datos: {e}")

    print("\n[+] Servidor backend de Vasconcellos Automotriz ejecutandose.")
    print(f"[*] URL Local: http://127.0.0.1:{Config.PORT}")
    print(f"[*] Motor de BD: {Config.DB_ENGINE.upper()}\n")
    
    app.run(host="0.0.0.0", port=Config.PORT, debug=Config.DEBUG)
