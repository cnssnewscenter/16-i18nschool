class ReversedProxyMiddleware():
    def process_request(self, request):
        if "X-SCRIPT-NAME" in request.META and request.META['X-SCRIPT-NAME']:
            script_name = request.META['X-SCRIPT-NAME']
            print(request.path_info, script_name)
            if script_name and request.path_info.startswith(script_name):
                request.path_info = request.path_info[len(script_name):]
