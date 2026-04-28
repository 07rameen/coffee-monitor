from datetime import datetime

_listeners = {}

def on(event_name: str, handler):
    _listeners.setdefault(event_name, []).append(handler)

def emit(event_name: str, payload: dict):
    payload["event"] = event_name
    payload["event_time"] = datetime.utcnow().isoformat()
    print(f"[EVENT] {event_name} → {payload['machine_id']}")
    for handler in _listeners.get(event_name, []):
        handler(payload)
