def get_swagger_spec():
    """
    Returns OpenAPI / Swagger specifications for public API consumers.
    """
    return {
        "openapi": "3.0.0",
        "info": {"title": "OmniThread OS Public API", "version": "6.0.0"},
        "paths": {"/api/v1/telemetry": {"post": {"description": "Ingest live metrics"}}}
    }

if __name__ == '__main__':
    print(get_swagger_spec())
