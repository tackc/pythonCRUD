from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse, Http404
from .models import Request
import datetime
from django.utils import timezone
from cpuinfo import get_cpu_info

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
    method = request.method
    time = datetime.datetime.now(tz=timezone.utc)

    Request.objects.create(requestType=method, requestTime=time)
    cpuInfo = get_cpu_info

    requests = Request.objects.order_by("-id")[:10]
    return render(request, 'requests/index.html', { 'requests': requests, 'cpuInfo': cpuInfo })

def requests_detail(request, request_id):
    try:
        details = Request.objects.get(id=request_id)
    except Request.DoesNotExist:
        raise Http404
    return render(request, 'requests/detail.html', { 'details': details })
