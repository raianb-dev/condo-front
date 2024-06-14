from django.shortcuts import redirect
import json
import requests

class MeuMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Verifica se a rota atual é a página de login
        if request.path == '/':
            # Se for a página de login, continua com a solicitação sem aplicar o middleware
            response = self.get_response(request)

            return response

        # Obtém o token da sessão
        data_string = request.session.get('data')
        if data_string:
            data = json.loads(data_string)
            access_token = data.get('access_token')

            # Verifica se o usuário está autenticado e possui um token na sessão
            if access_token:
                # Se o usuário estiver autenticado e tiver um token, verifica se há argumentos na URL
                allowed_routes = ['/', '/painel', '/v1/api/account/login', '/register-order']
                if request.path not in allowed_routes:
                    # Se houver argumentos na URL, redireciona para /painel/
                    return redirect('/painel')
            else:
                # Redireciona para a página de login se o usuário não tiver um token válido
                return redirect('login')
        else:
            # Redireciona para a página de login se não houver dados na sessão
            return redirect('login')

        try:
            # Se o usuário estiver autenticado e tiver um token, continua com a solicitação
            response = self.get_response(request)
            return response
        except requests.RequestException as e:
            # Trata erros de conexão com a API do backend
            # Aqui você pode redirecionar para uma página de erro ou exibir uma mensagem para o usuário
            return redirect('/')  # Substitua 'error_page' pelo nome da página de erro desejada