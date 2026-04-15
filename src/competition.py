"""Builder's competition module — track build stats."""
import json, os
from datetime import date

def record_build(artifact: str, category: str):
    """Record a build for the competition."""
    log_file = "build_log.json"
    log = []
    if os.path.exists(log_file):
        with open(log_file) as f:
            log = json.load(f)
    log.append({
        "date": date.today().isoformat(),
        "artifact": artifact,
        "category": category
    })
    with open(log_file, "w") as f:
        json.dump(log, f, indent=2)
    return len(log)

def get_stats():
    """Get my competition stats."""
    if not os.path.exists("build_log.json"):
        return {"total": 0, "categories": {}}
    with open("build_log.json") as f:
        log = json.load(f)
    cats = {}
    for entry in log:
        cats[entry["category"]] = cats.get(entry["category"], 0) + 1
    return {"total": len(log), "categories": cats}

if __name__ == "__main__":
    print(json.dumps(get_stats(), indent=2))
