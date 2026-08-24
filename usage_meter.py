def track_customer_usage(active_servers, metrics_collected):
    """
    Meters customer resource consumption for billing and usage limits.
    """
    usage_data = {
        "connected_servers": active_servers,
        "total_metrics_processed": metrics_collected,
        "billing_unit": "Standard Enterprise Pack"
    }
    print(f"[Usage Meter] Tracked {active_servers} active servers.")
    return usage_data

if __name__ == '__main__':
    track_customer_usage(45, 1250000)
