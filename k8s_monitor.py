import json

def check_kubernetes_health():
    """
    Simulates Kubernetes API connection, pod monitoring, and node health.
    """
    cluster_status = {
        "cluster_name": "omnithread-k8s-prod",
        "nodes": [
            {"node": "worker-node-01", "status": "Healthy", "cpu_load": "42%"},
            {"node": "worker-node-02", "status": "Warning", "cpu_load": "89%"}
        ],
        "pods": [
            {"pod_name": "auth-service-7b5c", "restarts": 0, "status": "Running"},
            {"pod_name": "payment-api-9x2q", "restarts": 3, "status": "CrashLoopBackOff"}
        ]
    }
    print("[K8s Monitor] Kubernetes cluster metrics fetched successfully.")
    return cluster_status

if __name__ == '__main__':
    print(json.dumps(check_kubernetes_health(), indent=2))
