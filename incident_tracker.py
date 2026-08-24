def create_incident(title, severity):
    """
    Tracks and assigns infrastructure incidents.
    """
    incident = {
        "id": "INC-8832",
        "title": title,
        "severity": severity,
        "status": "Open",
        "assigned_to": "On-Call DevOps Engineer"
    }
    print(f"[Incident Tracker] Created Incident #{incident['id']} -> {title}")
    return incident

if __name__ == '__main__':
    create_incident("API Gateway Latency Spike", "High")
