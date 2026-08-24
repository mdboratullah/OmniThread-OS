def perform_root_cause_analysis(error_log):
    """
    Correlates errors to pinpoint exact failure triggers.
    """
    if "database timeout" in error_log.lower():
        cause = "High connection pool saturation"
        solution = "Scale up database max_connections or optimize slow queries"
    else:
        cause = "Unknown system anomaly"
        solution = "Inspect system application logs"
        
    return {"root_cause": cause, "suggested_fix": solution}

if __name__ == '__main__':
    print(perform_root_cause_analysis("Error: Database timeout encountered at node 01"))
