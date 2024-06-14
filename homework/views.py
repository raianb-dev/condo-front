from django.shortcuts import render
import requests
import json
from datetime import datetime

def redirect_home(request):
    data_login = request.GET.get('data')
    skip = 0
    limit = 5
    if request.method == 'POST':
        limit = request.POST.get('limit')
        skip_value = request.POST.get('skip', '')  # Evita que seja uma string vazia
        skip = int(skip_value) if skip_value else 0  # Se skip_value estiver vazio, atribui 0
    response = requests.get(f'https://api.appdominio.pro/v1/api/orders?clientId=87010f8c-e1fe-4ac4-a4f3-7d2667c7662e&skip={skip}&limit={limit}')
    data = response.json()
    
    # Formate a data antes de passá-la para o template
    formatted_data = []
    for item in data['content']:
        # Converta a string da data para um objeto datetime
        date_in = datetime.strptime(item['date_in'], '%Y-%m-%d %H:%M:%S.%f')
        # Formate a data como desejado
        item['date_in'] = date_in.strftime('%d/%m/%Y %H:%M')
        formatted_data.append(item)
        

    return render(request, 'homework.html', {'data': formatted_data, 'skip': skip})
