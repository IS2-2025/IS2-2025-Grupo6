import sqlite3
from pathlib import Path

path: str = Path(__file__).parent
db_path: str = path / "test.db"

conexion = sqlite3.connect(db_path)

print("Conexion exitosa: ")