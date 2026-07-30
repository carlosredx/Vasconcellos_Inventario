from flask import Blueprint, request, jsonify
from backend.app.models.compra_model import CompraModel

compras_bp = Blueprint("compras", __name__)

@compras_bp.get("/compras")
def compras_get():
    """Lista todas las compras del inventario."""
    compras = CompraModel.get_all()
    return jsonify(compras)

@compras_bp.post("/compras")
def compras_post():
    """Registra una compra de reabastecimiento."""
    data = request.get_json(force=True)
    producto_id = data["producto_id"]
    cantidad = data["cantidad"]
    precio_compra = data["precio_compra"]

    success, msg = CompraModel.create(producto_id, cantidad, precio_compra)
    return jsonify({"msg": msg})

@compras_bp.delete("/compras/<int:id>")
def compras_delete(id):
    """Elimina una compra y descuenta el stock previamente sumado."""
    success, msg, status_code = CompraModel.delete(id)
    if not success:
        return jsonify({"error": msg}), status_code

    return jsonify({"msg": msg})
