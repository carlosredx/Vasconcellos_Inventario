-- Tablas para PostgreSQL

DROP TABLE IF EXISTS ventas;
DROP TABLE IF EXISTS compras;
DROP TABLE IF EXISTS movimientos;
DROP TABLE IF EXISTS lavados;
DROP TABLE IF EXISTS productos;

CREATE TABLE productos (
  id SERIAL PRIMARY KEY,
  nombre_producto VARCHAR(255) NOT NULL,
  etiqueta VARCHAR(100) DEFAULT NULL,
  precio DECIMAL(10,2) DEFAULT NULL,
  stock INT DEFAULT NULL
);

CREATE TABLE compras (
  id SERIAL PRIMARY KEY,
  producto_id INT NOT NULL,
  cantidad INT NOT NULL,
  precio_compra DECIMAL(10,2) DEFAULT NULL,
  total_compra DECIMAL(10,2) DEFAULT NULL,
  fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT compras_ibfk_1 FOREIGN KEY (producto_id) REFERENCES productos (id)
);

CREATE TABLE lavados (
  id SERIAL PRIMARY KEY,
  tipo VARCHAR(255) NOT NULL,
  precio INT NOT NULL,
  fecha TIMESTAMP NOT NULL,
  detalles TEXT
);

CREATE TABLE movimientos (
  id SERIAL PRIMARY KEY,
  producto_id INT NOT NULL,
  tipo VARCHAR(50) NOT NULL,
  cantidad INT NOT NULL,
  fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT movimientos_ibfk_1 FOREIGN KEY (producto_id) REFERENCES productos (id)
);

CREATE TABLE ventas (
  id SERIAL PRIMARY KEY,
  producto_id INT NOT NULL,
  cantidad INT NOT NULL,
  precio_unitario DECIMAL(10,2) NOT NULL,
  total DECIMAL(10,2) NOT NULL,
  fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  CONSTRAINT ventas_ibfk_1 FOREIGN KEY (producto_id) REFERENCES productos (id)
);

-- Datos Base
INSERT INTO productos (id, nombre_producto, etiqueta, precio, stock) VALUES 
(1,'HYUNDAI Teer G700 SP 10W-40','Aceite Motor',2000.00,9),
(2,'HYUNDAI Teer D700 C2/C3 5W-30','Aceite Motor',0.00,0),
(3,'MORE Ciclón SAE 20W/50','Aceite Motor',0.00,0),
(4,'LUBRAX Tecno Si 10W-40','Aceite Motor',0.00,0),
(5,'Shell Helix HX7 10W-40','Aceite Motor',0.00,0),
(6,'Shell Helix HX8 Profesional 5W-30','Aceite Motor',0.00,0),
(7,'Quartz 7000 10W-40','Aceite Motor',0.00,0),
(8,'Quartz Ineo MCS 5W-30','Aceite Motor',0.00,0),
(9,'Mobil Super 2000 10W-40','Aceite Motor',0.00,0),
(10,'Mobil Super 3000 5W-30','Aceite Motor',0.00,0),
(11,'Energy Premium 7908 SAE 5W-30','Aceite Motor',0.00,0),
(12,'Energy Premium 7508 Mannol 5W-30','Aceite Motor',0.00,0),
(13,'Classic 7501 Mannol 10W-40','Aceite Motor',0.00,0),
(14,'Motul 6100 Syn-clean FE 5W-30','Aceite Motor',0.00,0),
(15,'Liqui Moly 10W-40 Super Leichtlauf','Aceite Motor',0.00,0),
(16,'Engine Oil 9976 Senfineco','Aceite Motor',0.00,0),
(17,'DEXRON /// LUBRAX ATF TDX','Transmisión',0.00,0),
(18,'VISTONY GEAR OIL Synthetic 75W-90','Transmisión',0.00,0),
(19,'Fuel Injector Cleaner Senfineco','Aditivo',0.00,0),
(20,'Brake Fluid DOT 3 Synthetic','Aditivo',0.00,0),
(21,'DPF Foam Cleaner','Aditivo',0.00,0),
(22,'Anticongelante Refrigerante 50/50 Ciclón','Refrigerante',0.00,0),
(23,'Ice Freeze 33% Orgánico Vistony','Refrigerante',0.00,0),
(24,'Anticongelante Ciclón 33%','Refrigerante',0.00,0),
(25,'Coolant 715 Anticongelante','Refrigerante',0.00,0),
(26,'Ciclón Coolant B-712','Refrigerante',0.00,0),
(27,'Coolant Diesel Anticongelante','Refrigerante',0.00,0),
(28,'Líquido para radiador verde','Refrigerante',0.00,0),
(29,'Líquido para radiador rojo','Refrigerante',0.00,0),
(30,'Agua desmineralizada','Refrigerante',0.00,0),
(31,'Tapia Lavado en seco','Limpieza Exterior',0.00,0),
(32,'Tapia Shampoo cera con carnauba','Limpieza Exterior',0.00,0),
(33,'MAGIO COLOR CAR WASH WAX WATER','Limpieza Exterior',0.00,0),
(34,'Cera Carnauba','Limpieza Exterior',0.00,0),
(35,'Black Ciclón','Limpieza Exterior',0.00,0),
(36,'Frutes Ciclón','Limpieza Exterior',0.00,0),
(37,'Ice Blue Ciclón','Limpieza Exterior',0.00,0),
(38,'Shampoo concentrado','Limpieza Exterior',0.00,0),
(39,'Arlon Pintura Spray','Pintura',0.00,0),
(40,'Strong Ultra Seal','Protección',0.00,0),
(41,'GUYS HIGH GLOSS','Cera Detailing',0.00,0),
(42,'CHEMICAL GUYS ACTIVE FUSION SHINE','Cera Detailing',0.00,0),
(43,'EMICA CIELOM GUYS SHINE SPEED WIPE','Cera Detailing',0.00,0),
(44,'Fabric Clean','Limpieza Interior',0.00,0),
(45,'INNER CLEAN Interior Quick Detailer','Limpieza Interior',0.00,0),
(46,'Tapia Plastic Restorer','Limpieza Interior',0.00,0),
(47,'Tapia Protection Pro','Limpieza Interior',0.00,0),
(48,'CHEMICAL GUYS Leather Cleaner/Conditioner','Limpieza Interior',0.00,0),
(49,'Arlon limpia tapiz espuma','Limpieza Interior',0.00,0),
(50,'AllClean All Purpose Cleaner Degreaser','Limpieza Interior',0.00,0),
(51,'Water Stain Cleaner Deep Cleaner','Limpieza Interior',0.00,0),
(52,'Water Spot Remover','Limpieza Interior',0.00,0),
(53,'STRONG R GLASS CLEANER','Vidrios',0.00,0),
(54,'Anti empañante','Vidrios',0.00,0),
(55,'Limpia parabrisas','Vidrios',0.00,0),
(56,'Desengrasante de motor','Motor',0.00,0),
(57,'Limpia contactos eléctricos','Motor',0.00,0),
(58,'Renovador de neumáticos','Renovadores',0.00,0),
(59,'Silicona para tableros','Renovadores',0.00,0),
(60,'Silicona aromática','Renovadores',0.00,0),
(61,'Desodorante neutralizador tabaco','Aromas',0.00,0),
(62,'Little Trees','Aromas',0.00,0),
(63,'Limpiador de llantas','Llantas',0.00,0),
(64,'Wheel Hub Cleaner STRONG CLEANER','Llantas',0.00,0),
(65,'POLISHING AGENT W21','Pulido',0.00,0),
(66,'STRONG FINAL TOUGH','Pulido',0.00,0),
(67,'HEAVY D METAL POLISH','Pulido',0.00,0),
(68,'Batería Platin Silver','Accesorio',0.00,0),
(69,'BRM Plumilla Universal','Accesorio',0.00,0),
(70,'Pinturas colores','Pintura',0.00,0);

-- Ajustar las secuencias después del insert explícito para evitar colisiones
SELECT setval(pg_get_serial_sequence('productos', 'id'), (SELECT MAX(id) FROM productos) + 1);

INSERT INTO compras (producto_id, cantidad, precio_compra, total_compra, fecha) VALUES 
(1,21,400.00,8400.00,'2025-11-28 01:43:49');

INSERT INTO lavados (tipo, precio, fecha, detalles) VALUES 
('lavado full',434000,'2025-11-28 01:44:24','don juan');

INSERT INTO movimientos (producto_id, tipo, cantidad, fecha) VALUES 
(1,'COMPRA',5,'2025-11-14 12:09:08'),
(1,'VENTA',2,'2025-11-14 12:09:49');

INSERT INTO ventas (producto_id, cantidad, precio_unitario, total, fecha) VALUES 
(1,12,2000.00,24000.00,'2025-11-28 01:44:02');
