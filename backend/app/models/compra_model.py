from backend.app.database.db import get_db

class CompraModel:
    """Modelo de datos para transacciones de Compras de inventario."""

    @staticmethod
    def get_all():
        """Lista todas las compras registradas ordenadas cronológicamente."""
        db = get_db()
        cur = db.cursor()
        cur.execute("""
            SELECT c.id, p.nombre_producto, c.cantidad, c.precio_compra,
                   c.total_compra, c.fecha
            FROM compras c
            JOIN productos p ON c.producto_id = p.id
            ORDER BY c.fecha ASC
        """)
        filas = cur.fetchall()
        db.close()
        return [
            {
                "id": f[0],
                "nombre_producto": f[1],
                "cantidad": f[2],
                "precio_compra": float(f[3]) if f[3] is not None else 0.0,
                "total_compra": float(f[4]) if f[4] is not None else 0.0,
                "fecha": str(f[5]),
            }
            for f in filas
        ]

    @staticmethod
    def create(producto_id, cantidad, precio_compra):
        """
        Registra una compra:
        - Calcula total de la compra
        - Incrementa el stock del producto
        - Inserta registro en la tabla compras
        """
        total = float(cantidad) * float(precio_compra)
        db = get_db()
        cur = db.cursor()

        cur.execute("""
            INSERT INTO compras (producto_id, cantidad, precio_compra, total_compra, fecha)
            VALUES (%s, %s, %s, %s, NOW())
        """, (producto_id, cantidad, precio_compra, total))

        cur.execute("UPDATE productos SET stock = stock + %s WHERE id=%s", (cantidad, producto_id))

        db.commit()
        db.close()
        return True, "ok"

    @staticmethod
    def delete(compra_id):
        """
        Elimina una compra:
        - Resta del stock la cantidad ingresada
        - Valida que no deje stock en negativo
        """
        db = get_db()
        cur = db.cursor()

        cur.execute("SELECT producto_id, cantidad FROM compras WHERE id=%s", (compra_id,))
        fila = cur.fetchone()

        if not fila:
            db.close()
            return False, "Compra no encontrada", 404

        producto_id, cantidad = fila[0], fila[1]

        cur.execute("SELECT stock FROM productos WHERE id=%s", (producto_id,))
        fila_stock = cur.fetchone()

        if not fila_stock:
            db.close()
            return False, "Producto no encontrado para la compra", 404

        stock_actual = fila_stock[0]

        if stock_actual < cantidad:
            db.close()
            return False, "No se puede eliminar la compra porque dejaría el stock negativo.", 400

        cur.execute("UPDATE productos SET stock = stock - %s WHERE id=%s", (cantidad, producto_id))
        cur.execute("DELETE FROM compras WHERE id=%s", (compra_id,))

        db.commit()
        db.close()
        return True, "ok", 200
