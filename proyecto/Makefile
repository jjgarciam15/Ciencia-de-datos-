.PHONY: install run check

install:
	uv sync --locked

run:
	uv run streamlit run src/proyecto/app.py

check:
	uv run python -m compileall -q src
