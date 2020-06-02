from django.shortcuts import render

def Boomerang_entertext(request):
    return render(request, 'enterText.html')

def Boomerang_analysis(request):
    return render(request, 'Analysis.html')
