from django.http.response import JsonResponse
from django.shortcuts import render

def test(request):
    return JsonResponse({"key":"Django is fun"})