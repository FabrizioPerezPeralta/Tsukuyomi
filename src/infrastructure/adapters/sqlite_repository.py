import sqlite3
import pandas as pd
import os
from typing import List
from src.domain.entities import Activity
from src.domain.ports import ActivityRepository

class SQLiteRepository(ActivityRepository):
    def __init__(self, db_path: str = "data/tsukuyomi.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        os.makedirs(os.path.dirname(self.db_path), exist_ok=True)
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS horarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                actividad TEXT NOT NULL,
                fase TEXT NOT NULL,
                inicio TEXT NOT NULL,
                fin TEXT NOT NULL,
                categoria TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def add_activity(self, activity: Activity) -> Activity:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO horarios (actividad, fase, inicio, fin, categoria) VALUES (?,?,?,?,?)",
                       (activity.actividad, activity.fase, activity.inicio, activity.fin, activity.categoria))
        activity.id = cursor.lastrowid
        conn.commit()
        conn.close()
        return activity

    def get_activities(self) -> List[Activity]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, actividad, fase, inicio, fin, categoria FROM horarios")
        rows = cursor.fetchall()
        conn.close()
        
        activities = []
        for row in rows:
            activities.append(Activity(
                id=row[0], actividad=row[1], fase=row[2], inicio=row[3], fin=row[4], categoria=row[5]
            ))
        return activities

    def delete_activity(self, activity_id: int) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM horarios WHERE id = ?", (activity_id,))
        conn.commit()
        conn.close()
