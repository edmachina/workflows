# Usar un stage base para instalar dependencias
FROM python:3.10-slim as base

WORKDIR /code

# Copiar solo requirements.txt para instalar dependencias
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Etapa FastAPI
FROM base as fastapi

WORKDIR /code/app
COPY ./app /code/app
ENV PYTHONPATH=/code

CMD ["uvicorn", "app.src.main:app", "--host", "0.0.0.0", "--port", "3035", "--log-level", "debug"]

# Etapa Temporal Worker
FROM base as worker

WORKDIR /code/workers
COPY ./workers /code/workers
ENV PYTHONPATH=/code

CMD ["python", "backend/workflow.py"]
