def detect_anomaly(cpu_history):
    """
    Analyzes metric trends to predict unusual behavior or spikes.
    """
    avg_cpu = sum(cpu_history) / len(cpu_history) if cpu_history else 0
    is_anomaly = True if avg_cpu > 80.0 else False
    
    result = {
        "average_cpu": avg_cpu,
        "anomaly_detected": is_anomaly,
        "risk_score": "High" if is_anomaly else "Low"
    }
    print(f"[AI Anomaly] Analysis complete. Anomaly Status: {is_anomaly}")
    return result

if __name__ == '__main__':
    detect_anomaly([75.0, 82.5, 91.0, 88.0])
