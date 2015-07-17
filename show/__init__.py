class ReversedProxyMiddleware():
    def process_request(self, request):
        if "X-SCRIPT-NAME" in request.META and request.META['X-SCRIPT-NAME']:
            script_name = request.META['X-SCRIPT-NAME']
            if 