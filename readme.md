# 🚗 Vasconcellos Automotriz — Control de Inventario

## 📖 Explicación del proyecto

Sistema web para la gestión de inventario, compras, ventas y servicios automotrices, implementando una arquitectura cliente-servidor mediante una API REST para la administración de la información.

### 🛠️ Tecnologías Utilizadas
- Python • Flask (API REST) • PostgreSQL • HTML5 • CSS3 • JavaScript Vanilla

## ☁️ Arquitectura y Despliegue

La aplicación en su entorno de producción se encuentra desplegada utilizando la siguiente infraestructura cloud:
- **Frontend**: Interfaz de usuario desplegada en **Vercel**.
- **Backend**: API REST con Flask alojada en **Render**.
- **Base de Datos**: PostgreSQL alojada en **Neon**.

## 📥 Instalación y Pruebas Locales

Este proyecto está configurado para funcionar localmente con SQLite para desarrollo rápido. Sigue los siguientes pasos para levantar ambos entornos (Backend y Frontend).

**Requisitos Previos:**
- Python 3.8+ instalado.
- Git instalado.

### 1. Configuración del backend

Abre una terminal en la raíz del proyecto.

```bash
# 1. Instalamos las dependencias
pip install -r backend/requirements.txt

# 2. Inicializar la Base de Datos Local (SQLite) con tablas y datos
python backend/database_schema/init_db.py

# 3. Iniciar el Servidor Backend
python backend/run.py
```
El servidor estará listo y escuchando en: 👉 `http://127.0.0.1:5000`

### 2. Configuración del frontend

El frontend ya se encuentra integrado. Una vez que el servidor backend esté en ejecución, simplemente abre tu navegador y navega a `http://127.0.0.1:5000` para acceder a la aplicación directamente.

## 🐙 Comandos para subir cambios a Git

Cuando realices modificaciones en el código y desees subirlas a tu repositorio en GitHub, utiliza los siguientes comandos:

```bash
# 1. Revisa qué archivos cambiaron
git status

# 2. Empaqueta los archivos modificados o creados que sí deben subirse
git add .

# 3. Crea el commit con un mensaje descriptivo
git commit -m "Actualización del proyecto"

# 4. Sube los cambios al repositorio
git push
```