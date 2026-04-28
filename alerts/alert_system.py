from storage.db import save_maintenance

def handle_overheating(payload: dict):
    machine_id = payload["machine_id"]
    temp = payload["temperature"]
    print(f"🚨 ALERT: {machine_id} overheating! Temp={temp}°C")

def handle_maintenance(payload: dict):
    machine_id = payload["machine_id"]
    cups = payload["cups_served"]
    print(f"🔧 MAINTENANCE: {machine_id} needs service — {cups} cups served")
    save_maintenance(machine_id, f"cups_served={cups}")

def handle_machine_error(payload: dict):
    machine_id = payload["machine_id"]
    print(f"❌ ERROR: {machine_id} reported error status!")
