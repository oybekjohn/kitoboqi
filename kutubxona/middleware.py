class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f'----- Ushbu |http://127.0.0.1:8000{request.path}| so\'rovidan OLDIN ----')
        response = self.get_response(request)
        print(f'----- Ushbu |http://127.0.0.1:8000{request.path}| so\'rovidan KEYIN ----')

        return response