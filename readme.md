# 🚗 Vasconcellos Automotriz — Control de Inventario

Sistema web completo para el control de inventarios, gestión de ventas, compras de insumos y registro de servicios/lavados automotrices. Diseñado con una arquitectura desacoplada de **Frontend** (interfaz gráfica) y **Backend** (API REST con Flask).

---

## 🛠️ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:
- **Python 3.8+** ([Descargar Python](https://www.python.org/downloads/))
- **Git** ([Descargar Git](https://git-scm.com/))

---

## 📥 Instalación y Pruebas Locales (Paso a Paso)

Este proyecto está configurado para funcionar **automáticamente con SQLite** en tu computadora local para que puedas desarrollar y hacer pruebas sin necesidad de configurar un servidor de base de datos.

### 1. Instalar las Dependencias
Como hemos actualizado el proyecto para soportar PostgreSQL en la nube, es vital instalar las nuevas dependencias (si ya lo hiciste antes, hazlo de nuevo):
```bash
pip install -r backend/requirements.txt
```

### 2. Inicializar la Base de Datos Local (SQLite)
Ejecuta el script para crear las tablas y cargar los productos base de Vasconcellos Automotriz en un archivo local (`database.db`):
```bash
python backend/database_schema/init_db.py
```

### 3. Iniciar el Servidor Backend
Inicia el servidor backend en ejecución:
```bash
python backend/run.py
```

El servidor estará listo y escuchando en: 👉 **`http://127.0.0.1:5000`**

### 4. Acceder al Frontend Local
Abre el archivo `frontend/index.html` en tu navegador usando **Live Server** (en VS Code). Se conectará automáticamente a tu API local.

---

## ☁️ Simular Producción con PostgreSQL (Opcional)

Si alguna vez quieres probar la aplicación localmente apuntando a tu base de datos **Neon (PostgreSQL)** en lugar de SQLite:
1. Asegúrate de tener tu archivo `backend/.env` (puedes copiar el `.env.example`).
2. Añade o modifica estas líneas:
   ```env
   DB_ENGINE=postgresql
   DATABASE_URL=postgres://tu_usuario:tu_password@ep-tu-host.neon.tech/vasconcellos-db?sslmode=require
   ```
3. Reinicia el servidor backend (`python backend/run.py`).

---

## 🖥️ Acceder a la Interfaz Web (Frontend)

Una vez iniciado el servidor backend (`python backend/run.py`), tienes dos formas de abrir la aplicación:

1. **Apertura Directa (Recomendado)**: Navega en tu navegador web a **`http://127.0.0.1:5000`**.
2. **Con Live Server**: Abre el archivo `frontend/index.html` en VS Code usando Live Server. Se conectará automáticamente a la API local.

---

## 🏗️ Estructura del Proyecto

```
Vasconcellos - Control de inventario/
├── backend/
│   ├── app/
│   │   ├── database/        # Gestor de base de datos
│   │   ├── models/          # Modelos de datos (Productos, Ventas, Compras, Lavados)
│   │   └── routes/          # Endpoints API (Blueprints)
│   ├── database_schema/     # Esquema SQL e init_db.py
│   ├── .env.example         # Plantilla de entorno (Subida a Git)
│   ├── requirements.txt     # Dependencias del servidor
│   └── run.py               # Ejecutable del servidor backend
├── frontend/
│   ├── index.html           # Vista principal
│   ├── css/style.css        # Estilos visuales
│   └── js/script.js         # Cliente JavaScript interactivo
├── .gitignore               # Excluye .env, base de datos local y temporales
└── README.md                # Guía de instalación y uso
```

---

## 🐙 Comandos para subir cambios a Git

Cuando realices modificaciones en el código y desees subirlas a tu repositorio en GitHub:

```bash
git add .
git commit -m "Actualización del proyecto"
git push origin main
```

*(El archivo `.gitignore` se encargará automáticamente de no subir tu base de datos local `database.db` ni las claves privadas de `.env`)*.