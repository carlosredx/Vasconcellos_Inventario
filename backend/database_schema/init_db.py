import sys
from pathlib import Path

# Agregar raíz al PYTHONPATH
root_dir = Path(__file__).resolve().parent.parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

from backend.app.config import Config
from backend.app.database.db import get_db

PRODUCTOS_INICIALES = [
    ("HYUNDAI Teer G700 SP 10W-40", "Aceite Motor", 2000.00, 9),
    ("HYUNDAI Teer D700 C2/C3 5W-30", "Aceite Motor", 0.00, 0),
    ("MORE Ciclón SAE 20W/50", "Aceite Motor", 0.00, 0),
    ("LUBRAX Tecno Si 10W-40", "Aceite Motor", 0.00, 0),
    ("Shell Helix HX7 10W-40", "Aceite Motor", 0.00, 0),
    ("Shell Helix HX8 Profesional 5W-30", "Aceite Motor", 0.00, 0),
    ("Quartz 7000 10W-40", "Aceite Motor", 0.00, 0),
    ("Quartz Ineo MCS 5W-30", "Aceite Motor", 0.00, 0),
    ("Mobil Super 2000 10W-40", "Aceite Motor", 0.00, 0),
    ("Mobil Super 3000 5W-30", "Aceite Motor", 0.00, 0),
    ("Energy Premium 7908 SAE 5W-30", "Aceite Motor", 0.00, 0),
    ("DEXRON /// LUBRAX ATF TDX", "Transmisión", 0.00, 0),
    ("VISTONY GEAR OIL Synthetic 75W-90", "Transmisión", 0.00, 0),
    ("Fuel Injector Cleaner Senfineco", "Aditivo", 0.00, 0),
    ("Brake Fluid DOT 3 Synthetic", "Aditivo", 0.00, 0),
    ("Anticongelante Refrigerante 50/50 Ciclón", "Refrigerante", 0.00, 0),
    ("Tapia Lavado en seco", "Limpieza Exterior", 0.00, 0),
    ("Tapia Shampoo cera con carnauba", "Limpieza Exterior", 0.00, 0),
    ("STRONG R GLASS CLEANER", "Vidrios", 0.00, 0),
    ("Desengrasante de motor", "Motor", 0.00, 0),
    ("Renovador de neumáticos", "Renovadores", 0.00, 0),
    ("Limpiador de llantas", "Llantas", 0.00, 0)
]

def init_db():
    print(f"[+] Inicializando base de datos usando motor: {Config.DB_ENGINE.upper()}...")
    schema_path = Path(__file__).resolve().parent / "schema.sql"
    
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()

    db = get_db()
    cur = db.cursor()

    if Config.DB_ENGINE == "sqlite":
        db.conn.executescript(schema_sql)
    else:
        statements = [stmt.strip() for stmt in schema_sql.split(";") if stmt.strip()]
        for stmt in statements:
            cur.execute(stmt)

    cur.execute("SELECT COUNT(*) FROM productos")
    count = cur.fetchone()[0]

    if count == 0:
        print("[+] Sembrando productos iniciales de Vasconcellos Automotriz...")
        for p in PRODUCTOS_INICIALES:
            cur.execute("""
                INSERT INTO productos (nombre_producto, etiqueta, precio, stock)
                VALUES (%s, %s, %s, %s)
            """, p)
        
        cur.execute("""
            INSERT INTO compras (producto_id, cantidad, precio_compra, total_compra, fecha)
            VALUES (1, 21, 400.00, 8400.00, NOW())
        """)
        cur.execute("""
            INSERT INTO ventas (producto_id, cantidad, precio_unitario, total, fecha)
            VALUES (1, 12, 2000.00, 24000.00, NOW())
        """)
        cur.execute("""
            INSERT INTO lavados (tipo, detalles, precio, fecha)
            VALUES ('Lavado Full', 'Don Juan - Vehículo Sedán', 434000, NOW())
        """)

    db.commit()
    db.close()
    print("[OK] Base de datos inicializada correctamente.")

if __name__ == "__main__":
    init_db()
