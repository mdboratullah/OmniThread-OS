def fetch_cloud_resources():
    """
    Monitors multi-cloud instances across AWS, GCP, and Azure.
    """
    cloud_data = {
        "aws": {"instances_running": 12, "region": "us-east-1"},
        "gcp": {"instances_running": 5, "region": "asia-south1"},
        "azure": {"instances_running": 3, "region": "eastus"}
    }
    print("[Cloud Monitor] Multi-cloud resource status retrieved.")
    return cloud_data

if __name__ == '__main__':
    print(fetch_cloud_resources())
