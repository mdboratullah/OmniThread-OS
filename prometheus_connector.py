import urllib.request
import json

def fetch_real_prometheus_metrics(prometheus_url="http://localhost:9090/api/v1/query?query=up"):
    """
    Connects to a real Prometheus or Kubernetes cluster endpoint 
    to extract live production metrics.
    """
    try:
        req = urllib.request.Request(prometheus_url, headers={'User-Agent': 'OmniThread-OS-Enterprise'})
        response = urllib.request.urlopen(req, timeout=3)
        data = json.loads(response.read().decode('utf-8'))
        print("Successfully fetched live telemetry from production Prometheus cluster.")
        return data
    except Exception as e:
        print(f"Prometheus connection offline or unreachable. Falling back to internal engine telemetry: {e}")
        return None

if __name__ == '__main__':
    fetch_real_prometheus_metrics()
