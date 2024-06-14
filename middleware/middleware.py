from django.shortcuts import redirect
import json
import requests

class MeuMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica se a rota atual é a página de login
        if request.path == '/':
            response = self.get_response(request)
            return response

        # Obtém o token da sessão
        data_string = request.session.get('data')
        if data_string:
            data = json.loads(data_string)
            access_token = data.get('access_token')

            # Verifica se o usuário está autenticado e possui um token na sessão
            if access_token:
                # Adicione '/docs' à lista de rotas permitidas
                allowed_routes = ['/', '/painel', '/v1/api/account/login', '/register-order', '/docs']
                if request.path not in allowed_routes:
                    return redirect('/painel')
            else:
                return redirect('login')
        else:
            return redirect('login')

        try:
            response = self.get_response(request)
            return response
        except requests.RequestException as e:
            return redirect('/')  # Substitua 'error_page' pelo nome da página de erro desejada
