import random
import time
import json
from datetime import datetime
from kinesis.stream import put_record 

MACHINES = ["machine_1", "machine_2", "machine_3"]

def generate_machine_data(machine_id: str) -> dict:
    return {
        "machine_id": machine_id,
        "timestamp": datetime.utcnow().isoformat(),
        "cups_served": random.randint(0, 600),
        "temperature": round(random.uniform(60.0, 95.0), 1),
        "status": random.choice(["active", "idle", "error"]),
    }

def stream_data(interval: int = 5):
    print("Data generator started. Sending every 5 seconds...\n")
    while True:
        for machine_id in MACHINES:
            data = generate_machine_data(machine_id)
            print(f"[GENERATOR] {json.dumps(data)}")
            put_record(data)
        time.sleep(interval)
