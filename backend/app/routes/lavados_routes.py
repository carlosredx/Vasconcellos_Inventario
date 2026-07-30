from flask import Blueprint, request, jsonify
from backend.app.models.lavado_model import LavadoModel

lavados_bp = Blueprint("lavados", __name__)

@lavados_bp.get("/lavados")
def lavados_get():
    """Lista todos los registros de lavados / servicios."""
    lavados = LavadoModel.get_all()
    return jsonify(lavados)

@lavados_bp.post("/lavados")
def lavados_post():
    """Registra un nuevo lavado o servicio."""
    data = request.get_json(force=True)
    tipo = data["tipo"]
    detalles = data["detalles"]
    precio = data["precio"]

    LavadoModel.create(tipo, detalles, precio)
    return jsonify({"msg": "ok"})

@lavados_bp.delete("/lavados/<int:id>")
def lavados_delete(id):
    """Elimina un lavado o servicio registrado."""
    LavadoModel.delete(id)
    return jsonify({"msg": "ok"})
