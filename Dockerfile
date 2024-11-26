# Usa una imagen base estable de Python
FROM python:3.13-slim

# Establece el directorio de trabajo
WORKDIR /CODE

# Establece el PYTHONPATH
ENV PYTHONPATH=/CODE

# Instala dependencias necesarias para la compilación
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Instala Rust para compilar extensiones necesarias
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH="/root/.cargo/bin:$PATH"

# Copia y instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /CODE

# Copia el resto del código
COPY . .

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003", "--reload"]