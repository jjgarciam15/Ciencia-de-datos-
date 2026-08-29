FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN python -m pip install --no-cache-dir uv

COPY proyecto/pyproject.toml proyecto/uv.lock proyecto/README.md ./
COPY proyecto/src ./src

RUN uv sync --no-dev

EXPOSE 8501

HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8501/_stcore/health')"

CMD ["uv", "run", "streamlit", "run", "src/proyecto/app.py", "--server.address=0.0.0.0", "--server.port=8501"]
