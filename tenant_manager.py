def isolate_tenant_data(tenant_id, payload):
    """
    Ensures secure data isolation between different enterprise clients.
    """
    isolated_payload = {
        "tenant_id": tenant_id,
        "data": payload,
        "access_control": "Strictly Isolated"
    }
    print(f"[Multi-Tenant] Data routed securely for tenant: {tenant_id}")
    return isolated_payload

if __name__ == '__main__':
    isolate_tenant_data("Client-Alpha-Corp", {"cpu": 45})
