from events.event_system import emit

TEMP_ALERT_THRESHOLD = 85.0
CUPS_MAINTENANCE_THRESHOLD = 500

def process(data: dict):
    machine_id = data["machine_id"]
    temp = data["temperature"]
    cups = data["cups_served"]
    status = data["status"]

    # clean data — skip corrupt records
    if not machine_id or temp is None or cups is None:
        print(f"[PROCESSOR] Skipping corrupt record: {data}")
        return

    print(f"[PROCESSOR] Processing {machine_id} — temp={temp}°C cups={cups} status={status}")

    if temp > TEMP_ALERT_THRESHOLD:
        emit("MachineOverheating", {**data})

    if cups > CUPS_MAINTENANCE_THRESHOLD:
        emit("MaintenanceRequired", {**data})

    if status == "error":
        emit("MachineError", {**data})
