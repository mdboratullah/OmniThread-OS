def generate_prometheus_metrics():
    """
    Exposes system metrics in Prometheus text-based format.
    """
    metrics = """
# HELP omnithread_cpu_usage_percentage Current CPU usage
# TYPE omnithread_cpu_usage_percentage gauge
omnithread_cpu_usage_percentage{node="node-01"} 45.5

# HELP omnithread_ram_usage_percentage Current RAM usage
# TYPE omnithread_ram_usage_percentage gauge
omnithread_ram_usage_percentage{node="node-01"} 62.1
    """
    return metrics.strip()

if __name__ == '__main__':
    print(generate_prometheus_metrics())
