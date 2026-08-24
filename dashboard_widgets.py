def get_widget_config():
    """
    Returns layout definitions for advanced enterprise dashboard widgets.
    """
    return {
        "widgets": ["CPU Gauge", "Memory Trend Line", "Incident Heatmap", "Network Map"]
    }

if __name__ == '__main__':
    print(get_widget_config())
