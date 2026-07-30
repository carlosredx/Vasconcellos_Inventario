from pathlib import Path
from flask import Flask, send_from_directory
from flask_cors import CORS
from backend.app.config import Config
from backend.app.routes import productos_bp, ventas_bp, compras_bp, lavados_bp

def create_app(config_class=Config):
    """
    Application Factory para Flask.
    Configura CORS, registra blueprints de rutas y gestiona archivos estáticos.
    """
    frontend_dir = Path(__file__).resolve().parent.parent.parent / "frontend"

    app = Flask(__name__, static_folder=str(frontend_dir), static_url_path="")
    app.config.from_object(config_class)

    # Habilitar CORS
    CORS(app)

    # Registrar Blueprints de Rutas
    app.register_blueprint(productos_bp)
    app.register_blueprint(ventas_bp)
    app.register_blueprint(compras_bp)
    app.register_blueprint(lavados_bp)

    # Servir la app frontend directamente desde Flask
    @app.route("/")
    def index():
        return send_from_directory(app.static_folder, "index.html")

    @app.route("/<path:path>")
    def static_proxy(path):
        return send_from_directory(app.static_folder, path)

    return app
