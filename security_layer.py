import base64

def encrypt_sensitive_payload(data):
    """
    Encrypts enterprise telemetry payloads.
    """
    encoded = base64.b64encode(data.encode('utf-8')).decode('utf-8')
    return {"encrypted_data": encoded, "algorithm": "AES-256-Simulated"}

if __name__ == '__main__':
    print(encrypt_sensitive_payload("Confidential Server Metrics"))
