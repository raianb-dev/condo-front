from django.shortcuts import render, redirect
from django.urls import reverse
import requests
import json
import base64
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def redirectorder(request):
    if request.method == 'POST':
        client_id = "87010f8c-e1fe-4ac4-a4f3-7d2667c7662e"
        barcode = request.POST.get('barcode')
        apt = request.POST.get('apt')
        block = request.POST.get('block')
        image_base64 = request.POST.get('image_base64')

        if not image_base64:
            return redirect(reverse('homework'))

        data = {
            "clientId": client_id,
            "barcode": barcode,
            "apto": apt,
            "block": block
        }

        req = requests.post(url="http://api.appdominio.pro/v1/api/order", json=data)
        req_json = req.json()

        if "content" in req_json and "id" in req_json["content"]:
            order_id = req_json["content"]["id"]

            if order_id:
                image_data = {
                    "orderId": order_id,
                    "base64": image_base64
                }

                req_image = requests.post(url="http://api.appdominio.pro/v1/api/order/image", json=image_data)
                print(req_image.text)

        return redirect(reverse('homework'))
    return render(request, 'register.html')
