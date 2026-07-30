from backend.app.database.db import get_db

class VentaModel:
    """Modelo de datos para transacciones de Ventas."""

    @staticmethod
    def get_all():
        """Lista todas las ventas ordenadas cronológicamente."""
        db = get_db()
        cur = db.cursor()
        cur.execute("""
            SELECT v.id, p.nombre_producto, v.cantidad, v.precio_unitario, v.total, v.fecha
            FROM ventas v
            JOIN productos p ON v.producto_id = p.id
            ORDER BY v.fecha ASC
        """)
        filas = cur.fetchall()
        db.close()
        return [
            {
                "id": f[0],
                "nombre_producto": f[1],
                "cantidad": f[2],
                "precio_unitario": float(f[3]) if f[3] is not None else 0.0,
                "total": float(f[4]) if f[4] is not None else 0.0,
                "fecha": str(f[5]),
            }
            for f in filas
        ]

    @staticmethod
    def create(producto_id, cantidad):
        """
        Registra una venta:
        - Obtiene precio y verifica stock
        - Descuenta stock del producto
        - Inserta registro en la tabla ventas
        """
        db = get_db()
        cur = db.cursor()

        cur.execute("SELECT stock, precio FROM productos WHERE id=%s", (producto_id,))
        fila = cur.fetchone()

        if not fila:
            db.close()
            return False, "Producto no existe"

        stock_actual, precio_unitario = fila[0], fila[1]

        if stock_actual < cantidad:
            db.close()
            return False, "Stock insuficiente"

        total = float(precio_unitario) * cantidad

        # Registrar la venta
        cur.execute("""
            INSERT INTO ventas (producto_id, cantidad, precio_unitario, total, fecha)
            VALUES (%s, %s, %s, %s, NOW())
        """, (producto_id, cantidad, precio_unitario, total))

        # Descontar el stock
        cur.execute("UPDATE productos SET stock = stock - %s WHERE id=%s", (cantidad, producto_id))

        db.commit()
        db.close()
        return True, "ok"

    @staticmethod
    def delete(venta_id):
        """
        Elimina una venta y reestablece la cantidad de stock al producto.
        """
        db = get_db()
        cur = db.cursor()

        cur.execute("SELECT producto_id, cantidad FROM ventas WHERE id=%s", (venta_id,))
        fila = cur.fetchone()

        if not fila:
            db.close()
            return False, "Venta no encontrada"

        producto_id, cantidad = fila[0], fila[1]

        # Devolver stock
        cur.execute("UPDATE productos SET stock = stock + %s WHERE id=%s", (cantidad, producto_id))

        # Eliminar registro de venta
        cur.execute("DELETE FROM ventas WHERE id=%s", (venta_id,))

        db.commit()
        db.close()
        return True, "ok"
