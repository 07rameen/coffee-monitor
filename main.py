from data_generator.generator import stream_data
from processor.processor import process
from events.event_system import on
from alerts.alert_system import handle_overheating, handle_maintenance, handle_machine_error
from storage.db import init_db, save_log
from kinesis.stream import get_record
import threading 

def on_data_received(data: dict):
    save_log(data)
    process(data)

if __name__ == "__main__":
    init_db()

    # wire events to alert handlers
    on("MachineOverheating", handle_overheating)
    on("MaintenanceRequired", handle_maintenance)
    on("MachineError", handle_machine_error)

    print("=== Coffee Monitor Started ===\n")
    t = threading.Thread(target=stream_data)
    t.start()
    while True:
        data = get_record()
        save_log(data)
        process(data)

    
