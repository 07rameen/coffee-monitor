import sqlite3
from datetime import datetime

DB_PATH = "coffee_monitor.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS machine_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            machine_id TEXT,
            timestamp TEXT,
            cups_served INTEGER,
            temperature REAL,
            status TEXT
        )
    """)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS maintenance_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            machine_id TEXT,
            reason TEXT,
            logged_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_log(data: dict):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO machine_logs (machine_id, timestamp, cups_served, temperature, status) VALUES (?,?,?,?,?)",
        (data["machine_id"], data["timestamp"], data["cups_served"], data["temperature"], data["status"])
    )
    conn.commit()
    conn.close()

def save_maintenance(machine_id: str, reason: str):
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        "INSERT INTO maintenance_log (machine_id, reason, logged_at) VALUES (?,?,?)",
        (machine_id, reason, datetime.utcnow().isoformat())
    )
    conn.commit()
    conn.close()

def get_latest_logs(limit: int = 20) -> list:
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute(
        "SELECT * FROM machine_logs ORDER BY id DESC LIMIT ?", (limit,)
    ).fetchall()
    conn.close()
    return rows
