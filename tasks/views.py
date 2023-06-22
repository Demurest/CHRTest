from django.shortcuts import render, redirect
from .models import Jurisprudencias
import requests
import json
from django.core.paginator import Paginator


def buscarJurisprudencias(request):
    
    url = "https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list"
    
    payload = {
        "page":1,
        "pageSize":10,
        "search":request.POST['task'],
        "orden":"nuevo"
        
    }
    headers = {
        "Content-Type": "application/json",
        
    }

    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:  # Verifica que la solicitud haya sido exitosa
        try:
            data = response.json()

            juris = data['jurisprudencias']
            for item in juris:
                jurisprudencia = Jurisprudencias(
                tipoCausa=item['tipoCausa'],
                rol =item['rol'],
                caratula =item['caratula'],
                nombreProyecto =item['nombreProyecto'],
                descriptores = item['descriptores']
                )
                jurisprudencia.save()
            tasks= Jurisprudencias.objects.all()
        except requests.exceptions.JSONDecodeError as e:
            print("Error al decodificar JSON:", e)
    return render(request, 'list_tasks.html', {"tasks":tasks})

def list_tasks(request):

    #pagina principal
    
    return render(request, 'list_tasks.html')
