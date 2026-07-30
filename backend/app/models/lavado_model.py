from backend.app.database.db import get_db

class LavadoModel:
    """Modelo de datos para servicios y lavados."""

    @staticmethod
    def get_all():
        """Lista todos los registros de servicios/lavados."""
        db = get_db()
        cur = db.cursor()
        cur.execute("""
            SELECT id, tipo, detalles, precio, fecha
            FROM lavados
            ORDER BY fecha ASC
        """)
        filas = cur.fetchall()
        db.close()
        return [
            {
                "id": f[0],
                "tipo": f[1],
                "detalles": f[2],
                "precio": float(f[3]) if f[3] is not None else 0.0,
                "fecha": str(f[4]),
            }
            for f in filas
        ]

    @staticmethod
    def create(tipo, detalles, precio):
        """Registra un nuevo lavado o servicio."""
        db = get_db()
        cur = db.cursor()
        cur.execute("""
            INSERT INTO lavados (tipo, detalles, precio, fecha)
            VALUES (%s, %s, %s, NOW())
        """, (tipo, detalles, precio))
        db.commit()
        db.close()
        return True

    @staticmethod
    def delete(lavado_id):
        """Elimina un lavado/servicio por ID."""
        db = get_db()
        cur = db.cursor()
        cur.execute("DELETE FROM lavados WHERE id=%s", (lavado_id,))
        db.commit()
        db.close()
        return True
