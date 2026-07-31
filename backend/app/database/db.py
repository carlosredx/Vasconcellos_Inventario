import sqlite3
import psycopg2
import psycopg2.extras
from urllib.parse import urlparse
from backend.app.config import Config

class DBWrapper:
    """Wrapper unificado para conexiones SQLite y PostgreSQL."""
    def __init__(self, engine=None):
        self.engine = engine or Config.DB_ENGINE
        if self.engine == "sqlite":
            self.conn = sqlite3.connect(Config.SQLITE_DB_PATH)
            self.conn.row_factory = sqlite3.Row
        elif self.engine == "postgresql":
            # Si se entrega DATABASE_URL se usa directamente, sino se puede parsear
            if Config.DATABASE_URL:
                self.conn = psycopg2.connect(Config.DATABASE_URL, cursor_factory=psycopg2.extras.DictCursor)
            else:
                raise ValueError("DATABASE_URL no está configurada para PostgreSQL")
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
            self.conn.rollback()
        else:
            self.commit()
        self.close()

class DBCursor:
    """Cursor adaptable para transiciones transparentes entre SQLite y PostgreSQL."""
    def __init__(self, conn, engine):
        self.conn = conn
        self.engine = engine
        self.raw_cursor = conn.cursor()

    def execute(self, query, params=None):
        if params is None:
            params = ()
        if self.engine == "sqlite":
            # SQLite usa ? en vez de %s para parámetros, y CURRENT_TIMESTAMP en vez de NOW()
            query_sqlite = query.replace("%s", "?").replace("NOW()", "CURRENT_TIMESTAMP")
            return self.raw_cursor.execute(query_sqlite, params)
        else:
            # PostgreSQL usa %s como marcador por defecto en psycopg2
            return self.raw_cursor.execute(query, params)

    def fetchall(self):
        rows = self.raw_cursor.fetchall()
        if not rows:
            return rows
        if self.engine == "sqlite":
            return [tuple(row) for row in rows]
        # PostgreSQL con DictCursor, convertir a tupla para mantener compatibilidad
        return [tuple(row) for row in rows]

    def fetchone(self):
        row = self.raw_cursor.fetchone()
        if not row:
            return row
        if self.engine == "sqlite":
            return tuple(row)
        return tuple(row)

    @property
    def lastrowid(self):
        if self.engine == "sqlite":
            return self.raw_cursor.lastrowid
        else:
            # En PostgreSQL sin un RETURNING explícito en el execute, es difícil genérico, 
            # pero el frontend puede no necesitarlo si no lo estaba usando estrictamente.
            # (o podemos ajustarlo si fallan los INSERTS)
            return None

def get_db():
    """Retorna una instancia de la base de datos configurada."""
    return DBWrapper(Config.DB_ENGINE)
