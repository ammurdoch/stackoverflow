from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  # return HttpResponse("Hello, world. You're at the sorular index.")
  context = {}
  return render(request, 'index.html', context)

def ilk(request):
  return HttpResponse("Bu senin ilk sordugun soru")
