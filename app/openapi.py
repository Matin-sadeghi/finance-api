def configure_openapi(api):
    api.spec.components.security_scheme(
        "BearerAuth",
        {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        },
    )