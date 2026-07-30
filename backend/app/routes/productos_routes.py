from flask import Blueprint, request, jsonify
from backend.app.models.producto_model import ProductoModel

productos_bp = Blueprint("productos", __name__)

@productos_bp.get("/productos")
def productos_get():
    """Lista todos los productos del inventario."""
    productos = ProductoModel.get_all()
    return jsonify(productos)

@productos_bp.post("/productos")
def productos_post():
    """Crea un nuevo producto en el inventario."""
    data = request.get_json(force=True)
    ProductoModel.create(
        data["nombre_producto"],
        data["etiqueta"],
        data["stock"],
        data["precio"]
    )
    return jsonify({"msg": "ok"})

@productos_bp.put("/productos/<int:id>")
def productos_put(id):
    """Edita nombre, etiqueta, stock y precio de un producto."""
    data = request.get_json(force=True)
    ProductoModel.update(
        id,
        data["nombre_producto"],
        data["etiqueta"],
        data["stock"],
        data["precio"]
    )
    return jsonify({"msg": "ok"})

@productos_bp.delete("/productos/<int:id>")
def productos_del(id):
    """Elimina un producto por ID."""
    ProductoModel.delete(id)
    return jsonify({"msg": "ok"})

@productos_bp.get("/categorias")
def categorias_get():
    """Devuelve la lista de etiquetas de categorías únicas."""
    categorias = ProductoModel.get_categorias()
    return jsonify(categorias)
