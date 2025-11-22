class AppVersionMiddleware:
    """
    Middleware to extract mobile build version from headers.
    Adds `request.app_version` for backward compatibility support.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        version = (
            request.headers.get("Build-Version")
            or request.headers.get("X-App-Version")
            or None
        )

        request.app_version = version

        return self.get_response(request)
