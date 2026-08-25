def step_7_rbac(role, action):
    permissions = {"Admin": ["all"], "Engineer": ["read", "write"], "Viewer": ["read"]}
    return action in permissions.get(role, [])

def step_8_monitoring():
    return {"status": "Live Grafana & Prometheus metrics exporting", "history": "90-day retention"}

def step_9_ai_engine(cpu_load):
    if cpu_load > 85:
        return {"anomaly": True, "rca": "Memory leak / High traffic spike", "fix": "Scale container"}
    return {"anomaly": False, "rca": "Normal operation"}
