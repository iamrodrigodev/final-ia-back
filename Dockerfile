# Usa una imagen oficial de Python ligera como imagen base
FROM python:3.12-slim AS builder

# Evitar que Python genere archivos .pyc y permitir que los logs se muestren en tiempo real
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalar dependencias del sistema necesarias para compilar paquetes de Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Crear entorno virtual para mantener las dependencias aisladas
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el archivo de dependencias
COPY requirements.txt .

# Instalar dependencias dentro del entorno virtual
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# --- Etapa de producción ---
FROM python:3.12-slim AS runner

# Evitar que Python genere archivos .pyc y buffer de logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Crear un usuario no root para mejorar la seguridad
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el entorno virtual de la etapa anterior
COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copiar el código de la aplicación y asignar propiedad al usuario no root
COPY --chown=appuser:appuser . .

# Cambiar al usuario no root
USER appuser

# Exponer el puerto donde correrá FastAPI
EXPOSE 8000

# Comando para ejecutar la aplicación con Uvicorn en producción
CMD ["uvicorn", "main:aplicacion", "--host", "0.0.0.0", "--port", "8000"]
