from flask import Blueprint, request, jsonify
from backend.app.models.venta_model import VentaModel

ventas_bp = Blueprint("ventas", __name__)

@ventas_bp.get("/ventas")
def ventas_get():
    """Lista todas las ventas con información de productos."""
    ventas = VentaModel.get_all()
    return jsonify(ventas)

@ventas_bp.post("/ventas")
def ventas_post():
    """Registra una venta de producto."""
    data = request.get_json(force=True)
    producto_id = data["producto_id"]
    cantidad = data["cantidad"]

    success, msg = VentaModel.create(producto_id, cantidad)
    if not success:
        return jsonify({"error": msg}), 400

    return jsonify({"msg": msg})

@ventas_bp.delete("/ventas/<int:id>")
def ventas_delete(id):
    """Elimina una venta y restituye el stock."""
    success, msg = VentaModel.delete(id)
    if not success:
        return jsonify({"error": msg}), 404

    return jsonify({"msg": msg})
