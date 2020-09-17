from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Request

class RequestCreate(CreateView):
    model = Request
    fields = '__all__'

class RequestUpdate(UpdateView):
    model = Request
    fields = ['comment']

class RequestDelete(DeleteView):
    model = Request
    success_url = '/requests/'

def home(request):
    return render(request, 'requests/index.html')

def about(request):
    return render(request, 'about.html')

def requests_index(request):
    requests = Request.objects.all()
    return render(request, 'requests/index.html', { 'requests': requests })

def requests_detail(request, request_id):
    request = Request.objects.get(id=request_id)
    return render(request, 'requests/detail.html', { 'request': request })
