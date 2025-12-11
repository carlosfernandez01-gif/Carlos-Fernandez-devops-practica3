# Usar la imagen base ligera de Python
FROM python:3.12-slim

# Crear carpeta de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias y instalarlas
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY src/ ./src/

# Dar permisos (no siempre necesario, pero buena práctica)
RUN chmod -R 755 /app

# Comando de inicio
CMD ["python", "src/main.py"]
