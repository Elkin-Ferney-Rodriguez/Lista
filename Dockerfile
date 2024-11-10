# Usa una imagen base de Python
FROM python:3.13-slim

# Establece el directorio de trabajo
WORKDIR /CODE

# Añade esta línea para establecer el PYTHONPATH
ENV PYTHONPATH=/CODE

# Instala dependencias del sistema
RUN apt-get update && apt-get install -y git

# Copia el archivo requirements.txt
COPY requirements.txt .

# Instala las dependencias desde requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copia el resto del código del backend
COPY . .

# Exponer el puerto que usará la aplicación
EXPOSE 8002

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001", "--reload"]
