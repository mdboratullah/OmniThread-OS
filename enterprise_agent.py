import platform

def get_agent_specs():
    """
    Gathers host system information for enterprise deployment.
    """
    specs = {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "agent_version": "v6.0-Enterprise"
    }
    print(f"[Agent] Initialized on {specs['system']} ({specs['node']})")
    return specs

if __name__ == '__main__':
    get_agent_specs()
