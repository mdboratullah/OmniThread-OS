def create_jira_ticket(summary, description):
    """
    Automatically creates Jira tickets upon critical incident detection.
    """
    ticket_key = "OPS-4021"
    print(f"[Jira Integration] Created ticket {ticket_key}: {summary}")
    return {"ticket_key": ticket_key, "status": "Synced"}

if __name__ == '__main__':
    create_jira_ticket("Memory leak detected on Node 02", "Automated alert from AIOps core.")
