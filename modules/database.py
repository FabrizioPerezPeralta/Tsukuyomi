import sqlite3
import pandas as pd

DB_PATH = "data/tsukuyomi_core.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS horarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarea TEXT NOT NULL,
            fase TEXT, -- El "Día" será llamado Fase
            hora_inicio TIME,
            hora_fin TIME,
            prioridad TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_task(tarea, fase, inicio, fin, prioridad):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO horarios (tarea, fase, hora_inicio, hora_fin, prioridad) VALUES (?,?,?,?,?)",
                   (tarea, fase, str(inicio), str(fin), prioridad))
    conn.commit()
    conn.close()

def get_tasks():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM horarios", conn)
    conn.close()
    return df

def delete_task(id_tarea):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM horarios WHERE id = ?", (id_tarea,))
    conn.commit()
    conn.close()