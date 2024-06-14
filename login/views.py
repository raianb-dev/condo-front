from django.shortcuts import render, redirect
from django.urls import reverse
import requests
import json

def redirect_login(request):
    email = ''
    password = ''
    error_message = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        data = {
            "username": email,
            "pwd": password
        }
        status = requests.post(url='http://localhost:4000/v1/api/account/login', json=data)
        
        req = status.text
        data = json.loads(req)
        request.session['data'] = json.dumps(data)
        if status.status_code == 200:
            return redirect(reverse('homework'))
        else:
            error_message = data.get('error_message', 'Email ou senha invalidos')
    return render(request, "index.html", {'error_message': error_message, 'user': email, 'pwd':password})
