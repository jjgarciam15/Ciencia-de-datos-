# Laboratorio de ciencia de datos

Aplicación educativa construida con [Streamlit](https://streamlit.io/) para explorar conjuntos de datos sin escribir código. Permite cargar un archivo CSV, revisar una muestra, calcular métricas básicas, consultar estadísticas descriptivas y crear una gráfica interactiva. Si no se carga un archivo, la aplicación genera datos reproducibles de ejemplo.

## Estructura

```text
.
├── README.md
├── .gitignore
└── proyecto/
    ├── Makefile
    ├── pyproject.toml
    ├── uv.lock
    └── src/proyecto/
        ├── __init__.py
        └── app.py
```

- `app.py`: interfaz y lógica del dashboard.
- `pyproject.toml`: metadatos y dependencias directas.
- `uv.lock`: versiones resueltas para instalaciones reproducibles.
- `Makefile`: atajos para instalar, validar y ejecutar.

## Requisitos

- Python 3.12 o superior.
- [uv](https://docs.astral.sh/uv/).

Instala `uv` si todavía no está disponible:

```bash
python -m pip install uv
```

## Ejecutar localmente

Desde la raíz del repositorio:

```bash
cd proyecto
uv sync --locked
uv run streamlit run src/proyecto/app.py
```

También puedes usar los atajos:

```bash
cd proyecto
make install
make check
make run
```

Streamlit mostrará la URL local, normalmente `http://localhost:8501`.

## Usar la aplicación

1. Abre la URL mostrada por Streamlit.
2. Carga un archivo `.csv` desde la barra lateral o utiliza los datos de ejemplo.
3. Revisa las métricas, el resumen estadístico y la gráfica.
4. Selecciona las columnas que deseas visualizar.

Los CSV cargados se procesan en memoria durante la sesión. La aplicación no implementa cuentas de usuario ni almacenamiento persistente.

## Desplegar en Streamlit Community Cloud

1. Publica este repositorio en GitHub.
2. En [share.streamlit.io](https://share.streamlit.io/), crea una aplicación nueva.
3. Selecciona el repositorio y la rama `main`.
4. Usa esta ruta como archivo principal:

```text
proyecto/src/proyecto/app.py
```

Streamlit Cloud instalará las dependencias declaradas en `proyecto/pyproject.toml`. Si el servicio no detecta el archivo por estar en un subdirectorio, configura el directorio de trabajo como `proyecto`.

## Desplegar con Docker

Construye la imagen desde la raíz:

```bash
docker build -t laboratorio-datos .
```

Ejecuta el contenedor:

```bash
docker run --rm -p 8501:8501 laboratorio-datos
```

Después abre `http://localhost:8501`.

## Comprobación rápida

```bash
cd proyecto
uv sync --locked
uv run python -m compileall -q src
uv run streamlit run src/proyecto/app.py
```

## Licencia

Este proyecto se distribuye bajo la licencia incluida en [LICENSE](LICENSE).
