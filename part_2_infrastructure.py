def step_4_database():
    return {"primary": "PostgreSQL + TimescaleDB", "cache": "Redis In-Memory Cluster", "backup": "Automated Cron Snapshot"}

def step_5_agent():
    return {"agents_supported": ["Linux .deb", "Windows .msi", "Kubernetes DaemonSet"], "metrics": "CPU, RAM, Disk, Network live"}

def step_6_api_security():
    return {"gateway": "Kong/Custom API Gateway", "auth": "JWT & OAuth2", "encryption": "AES-256"}
