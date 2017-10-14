from django.shortcuts import render


def index(request):
    return render(request, 'df_user/index.html')

def register(request):
    return render(request, 'df_user/register.html')