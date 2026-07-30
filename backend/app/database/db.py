import sqlite3
import mysql.connector
from backend.app.config import Config

class DBWrapper:
    """Wrapper unificado para conexiones SQLite y MySQL."""
    def __init__(self, engine=None):
        self.engine = engine or Config.DB_ENGINE
        if self.engine == "sqlite":
            self.conn = sqlite3.connect(Config.SQLITE_DB_PATH)
            self.conn.row_factory = sqlite3.Row
        elif self.engine == "mysql":
            self.conn = mysql.connector.connect(
                host=Config.DB_HOST,
                port=Config.DB_PORT,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME
            )
        else:
            raise ValueError(f"Motor de base de datos no soportado: {self.engine}")

    def cursor(self):
        return DBCursor(self.conn, self.engine)

    def commit(self):
        self.conn.commit()

    def close(self):
        self.conn.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # Si ocurre error, rollback
            pass
        else:
            self.commit()
        self.close()

class DBCursor:
    """Cursor adaptable para transiciones transparentes entre SQLite y MySQL."""
    def __init__(self, conn, engine):
        self.conn = conn
        self.engine = engine
        self.raw_cursor = conn.cursor()

    def execute(self, query, params=None):
        if params is None:
            params = ()
        if self.engine == "sqlite":
            # Adaptar marcadores de parámetros MySQL (%s -> ?) y funciones temporales
            query_sqlite = query.replace("%s", "?").replace("NOW()", "CURRENT_TIMESTAMP")
            return self.raw_cursor.execute(query_sqlite, params)
        else:
            return self.raw_cursor.execute(query, params)

    def fetchall(self):
        rows = self.raw_cursor.fetchall()
        if self.engine == "sqlite" and rows:
            # Convertir sqlite3.Row a tupla de valores para mantener interfaz uniforme
            return [tuple(row) for row in rows]
        return rows

    def fetchone(self):
        row = self.raw_cursor.fetchone()
        if self.engine == "sqlite" and row:
            return tuple(row)
        return row

    @property
    def lastrowid(self):
        return self.raw_cursor.lastrowid

def get_db():
    """Retorna una instancia de la base de datos configurada."""
    return DBWrapper(Config.DB_ENGINE)
