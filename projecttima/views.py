from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

@login_required
def restricted_page(request):
    return HttpResponse("только для зарегистрированных пользователей")