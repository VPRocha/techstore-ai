from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA = DATA_DIR / "raw"
PROCESSED_DATA = DATA_DIR / "processed"

DATABASE_DIR = PROJECT_ROOT / "database"

MIGRATIONS_DIR = DATABASE_DIR / "migrations"
SEEDS_DIR = DATABASE_DIR / "seeds"
QUERIES_DIR = DATABASE_DIR / "queries"

DOCS_DIR = PROJECT_ROOT / "docs"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"