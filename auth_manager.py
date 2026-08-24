def verify_rbac_permission(role, action):
    """
    Role-Based Access Control handler for enterprise users.
    """
    permissions = {
        "Admin": ["read", "write", "delete", "deploy"],
        "Operator": ["read", "write"],
        "Viewer": ["read"]
    }
    
    allowed = action in permissions.get(role, [])
    return {"role": role, "action": action, "authorized": allowed}

if __name__ == '__main__':
    print(verify_rbac_permission("Operator", "delete"))
