from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

def Boomerang_entertext(request):
    return render(request, 'enterText.html')

def Boomerang_analysis(request):
    #def get(self, request, *args, **kwargs):
    return render(request, 'Analysis.html', {"hi":10})


def get_data(request, *args, **kwargs):
    data = {"sales":100,
            "customers": 10,
    }
    return JsonResponse(data)
