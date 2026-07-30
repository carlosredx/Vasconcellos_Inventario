-- ============================================================
-- ESQUEMA DE BASE DE DATOS - VASCONCELLOS AUTOMOTRIZ
-- Compatible con SQLite y MySQL
-- ============================================================

CREATE TABLE IF NOT EXISTS productos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  nombre_producto VARCHAR(255) NOT NULL,
  etiqueta VARCHAR(100) DEFAULT NULL,
  precio DECIMAL(10,2) DEFAULT 0.00,
  stock INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS ventas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  producto_id INT NOT NULL,
  cantidad INT NOT NULL,
  precio_unitario DECIMAL(10,2) NOT NULL,
  total DECIMAL(10,2) NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (producto_id) REFERENCES productos (id)
);

CREATE TABLE IF NOT EXISTS compras (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  producto_id INT NOT NULL,
  cantidad INT NOT NULL,
  precio_compra DECIMAL(10,2) DEFAULT 0.00,
  total_compra DECIMAL(10,2) DEFAULT 0.00,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (producto_id) REFERENCES productos (id)
);

CREATE TABLE IF NOT EXISTS lavados (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tipo VARCHAR(255) NOT NULL,
  precio DECIMAL(10,2) NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  detalles TEXT
);

CREATE TABLE IF NOT EXISTS movimientos (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  producto_id INT NOT NULL,
  tipo VARCHAR(50) NOT NULL,
  cantidad INT NOT NULL,
  fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (producto_id) REFERENCES productos (id)
);
