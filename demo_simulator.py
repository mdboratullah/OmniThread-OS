def trigger_demo_failure_simulation():
    """
    Simulates a controlled server failure to demonstrate AI recovery on public demo.
    """
    print("[Demo Mode] Simulating sudden CPU spike and memory bottleneck...")
    simulation_result = {
        "simulated_event": "Out of Memory (OOM)",
        "ai_prediction_time": "12 seconds prior",
        "auto_recovery_status": "Successful"
    }
    return simulation_result

if __name__ == '__main__':
    trigger_demo_failure_simulation()
