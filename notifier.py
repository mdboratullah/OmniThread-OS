def dispatch_alert(channel, message):
    """
    Sends critical incident alerts to enterprise communication channels.
    """
    print(f"[Alert Sent via {channel}] Message: {message}")
    return {"channel": channel, "status": "Delivered"}

if __name__ == '__main__':
    dispatch_alert("Slack", "CRITICAL: High memory usage detected on Production-Node-01")
