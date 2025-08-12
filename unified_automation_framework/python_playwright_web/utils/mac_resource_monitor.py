import psutil
import json

def get_mac_resources():
    data = {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "disk_usage": psutil.disk_usage('/')._asdict(),
        "virtual_memory": psutil.virtual_memory()._asdict()
    }
    return json.dumps(data, indent=4)