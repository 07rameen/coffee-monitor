from fastapi import FastAPI
from storage.db import get_latest_logs

app = FastAPI(title="Coffee Monitor Dashboard")

@app.get("/")
def root():
    return {"message": "Coffee Monitor is running!"}

@app.get("/machines")
def get_machines():
    rows = get_latest_logs(limit=50)
    machines = {}
    for row in rows:
        mid = row[1]
        if mid not in machines:
            machines[mid] = {
                "machine_id": mid,
                "last_seen": row[2],
                "cups_served": row[3],
                "temperature": row[4],
                "status": row[5],
            }
    return {"machines": list(machines.values())}

@app.get("/logs")
def get_logs():
    rows = get_latest_logs(limit=20)
    logs = [
        {
            "id": r[0],
            "machine_id": r[1],
            "timestamp": r[2],
            "cups_served": r[3],
            "temperature": r[4],
            "status": r[5],
        }
        for r in rows
    ]
    return {"logs": logs}
