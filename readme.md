# 🚗 Vasconcellos Automotriz — Control de Inventario

Sistema web completo para el control de inventarios, gestión de ventas, compras de insumos y registro de servicios/lavados automotrices. Diseñado con una arquitectura desacoplada de **Frontend** (interfaz gráfica) y **Backend** (API REST con Flask).

---

## 🛠️ Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:
- **Python 3.8+** ([Descargar Python](https://www.python.org/downloads/))
- **Git** ([Descargar Git](https://git-scm.com/))

---

## 📥 Instalación y Puesta en Marcha (Paso a Paso)

Sigue estos sencillos pasos para poner a funcionar el proyecto tras clonarlo desde GitHub:

### 1. Clonar el Repositorio
```bash
git clone <URL_DE_TU_REPOSITORIO>
cd "Vasconcellos - Control de inventario"
```

### 2. Crear el Archivo de Configuración `.env`
Copia la plantilla de variables de entorno `.env.example` para crear tu propio archivo `.env` local:

**En Windows (PowerShell / CMD):**
```powershell
copy backend\.env.example backend\.env
```

**En Linux / Mac / Git Bash:**
```bash
cp backend/.env.example backend/.env
```

### 3. Instalar las Dependencias de Python
Instala los paquetes necesarios ejecutando:
```bash
pip install -r backend/requirements.txt
```

### 4. Inicializar la Base de Datos Local
Ejecuta el script para crear las tablas y cargar los productos base de Vasconcellos Automotriz:
```bash
python backend/database_schema/init_db.py
```

### 5. Iniciar el Servidor Backend
Inicia el servidor backend en ejecución:
```bash
python backend/run.py
```

El servidor estará listo y escuchando en:
👉 **`http://127.0.0.1:5000`**

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