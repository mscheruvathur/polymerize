from rest_framework.response import Response

class RestResponse(Response):
    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type=None):
        self.status = "error" if status >= 299 else "success"
        self.headers = headers
        super().__init__(data, status, template_name, headers, exception, content_type)