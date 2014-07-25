from django.http import HttpResponse, Http404
from django.shortcuts import render
import KPIs.settings

def indicadores(request):	
	img ="images/KPIs-indicadores.png"
	return render (request, 'mockups.html', {'img':img})

def insertar(request):
	img ="images/KPIs-insertar.png"
	return render (request, 'mockups.html', {'img':img})

