import platform
import subprocess

class EnterpriseAgentDeployer:
    def __init__(self):
        self.os_type = platform.system()

    def generate_agent_package(self):
        if self.os_type == "Linux":
            return {"package": "omnithread-agent_6.0_amd64.deb", "command": "sudo dpkg -i omnithread-agent_6.0_amd64.deb"}
        elif self.os_type == "Windows":
            return {"package": "OmniThreadAgent-v6.0.msi", "command": "msiexec /i OmniThreadAgent-v6.0.msi /quiet"}
        else:
            return {"package": "Kubernetes DaemonSet YAML", "command": "kubectl apply -f agent-daemonset.yaml"}
