"""Aplicación principal del dashboard de ciencia de datos."""

from __future__ import annotations

from io import BytesIO

import numpy as np
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Laboratorio de datos",
    page_icon="📊",
    layout="wide",
)


@st.cache_data
def crear_datos_demo() -> pd.DataFrame:
    """Genera un conjunto reproducible para explorar la aplicación."""
    rng = np.random.default_rng(42)
    fechas = pd.date_range("2026-01-01", periods=180, freq="D")
    categorias = np.array(["Analítica", "Machine Learning", "Visualización"])

    return pd.DataFrame(
        {
            "fecha": fechas,
            "categoria": rng.choice(categorias, size=len(fechas)),
            "valor": rng.normal(100, 18, size=len(fechas)).round(2),
            "observaciones": rng.integers(10, 100, size=len(fechas)),
        }
    )


@st.cache_data
def leer_csv(contenido: bytes) -> pd.DataFrame:
    """Lee el CSV cargado sin conservar referencias al archivo temporal."""
    return pd.read_csv(BytesIO(contenido))


def mostrar_metricas(datos: pd.DataFrame) -> None:
    """Muestra un resumen compacto del conjunto de datos."""
    numericas = datos.select_dtypes(include="number")
    columnas = st.columns(3)
    columnas[0].metric("Filas", f"{len(datos):,}")
    columnas[1].metric("Columnas", len(datos.columns))
    columnas[2].metric("Valores ausentes", f"{int(datos.isna().sum().sum()):,}")

    if not numericas.empty:
        st.subheader("Resumen estadístico")
        st.dataframe(numericas.describe().T, use_container_width=True)


def mostrar_graficas(datos: pd.DataFrame) -> None:
    """Permite escoger columnas y construir una gráfica con datos numéricos."""
    numericas = datos.select_dtypes(include="number").columns.tolist()
    if not numericas:
        st.info("El archivo no contiene columnas numéricas para graficar.")
        return

    st.subheader("Exploración visual")
    eje_y = st.selectbox("Variable numérica", numericas)
    eje_x = st.selectbox("Eje horizontal", ["Índice", *datos.columns.tolist()])

    grafica = datos[[eje_y]].copy()
    if eje_x != "Índice":
        grafica.index = datos[eje_x]

    st.line_chart(grafica)


def main() -> None:
    """Renderiza la interfaz completa."""
    st.title("📊 Laboratorio de ciencia de datos")
    st.write(
        "Carga un archivo CSV para inspeccionarlo o utiliza los datos de ejemplo. "
        "La información se procesa únicamente durante la sesión de Streamlit."
    )

    with st.sidebar:
        st.header("Fuente de datos")
        archivo = st.file_uploader("Selecciona un CSV", type=["csv"])
        st.caption("Si no cargas un archivo se utilizará un conjunto reproducible de ejemplo.")

    try:
        datos = leer_csv(archivo.getvalue()) if archivo else crear_datos_demo()
    except (UnicodeDecodeError, pd.errors.ParserError, pd.errors.EmptyDataError) as error:
        st.error(f"No fue posible leer el CSV: {error}")
        st.stop()

    st.subheader("Vista previa")
    st.dataframe(datos.head(100), use_container_width=True)
    mostrar_metricas(datos)
    mostrar_graficas(datos)


if __name__ == "__main__":
    main()
