from backend.app.database.db import get_db

class ProductoModel:
    """Modelo de datos para la entidad Productos."""

    @staticmethod
    def get_all():
        """Obtiene la lista de todos los productos ordenados por ID."""
        db = get_db()
        cur = db.cursor()
        cur.execute("""
            SELECT id, nombre_producto, etiqueta, stock, precio
            FROM productos
            ORDER BY id ASC
        """)
        filas = cur.fetchall()
        db.close()
        return [
            {
                "id": f[0],
                "nombre_producto": f[1],
                "etiqueta": f[2],
                "stock": f[3],
                "precio": float(f[4]) if f[4] is not None else 0.0,
            }
            for f in filas
        ]

    @staticmethod
    def create(nombre_producto, etiqueta, stock, precio):
        """Crea un nuevo producto en la base de datos."""
        db = get_db()
        cur = db.cursor()
        cur.execute("""
            INSERT INTO productos (nombre_producto, etiqueta, stock, precio)
            VALUES (%s, %s, %s, %s)
        """, (nombre_producto, etiqueta, stock, precio))
        db.commit()
        db.close()
        return True

    @staticmethod
    def update(producto_id, nombre_producto, etiqueta, stock, precio):
        """Actualiza los datos de un producto existente."""
        db = get_db()
        cur = db.cursor()
        cur.execute("""
            UPDATE productos
            SET nombre_producto=%s, etiqueta=%s, stock=%s, precio=%s
            WHERE id=%s
        """, (nombre_producto, etiqueta, stock, precio, producto_id))
        db.commit()
        db.close()
        return True

    @staticmethod
    def delete(producto_id):
        """Elimina un producto por su ID."""
        db = get_db()
        cur = db.cursor()
        cur.execute("DELETE FROM productos WHERE id=%s", (producto_id,))
        db.commit()
        db.close()
        return True

    @staticmethod
    def get_categorias():
        """Retorna las etiquetas/categorías únicas de los productos."""
        db = get_db()
        cur = db.cursor()
        cur.execute("SELECT DISTINCT etiqueta FROM productos ORDER BY etiqueta ASC")
        filas = cur.fetchall()
        db.close()
        return [c[0] for c in filas if c[0]]
