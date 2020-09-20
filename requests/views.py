from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Request
import datetime
from django.utils import timezone
from cpuinfo import get_cpu_info_json

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
    path = request.path
    method = request.method
    time = datetime.datetime.now(tz=timezone.utc)

    r = Request.objects.create(requestType=method, requestTime=time)

    requests = Request.objects.order_by("-id")[:10]
    return render(request, 'requests/index.html', { 'requests': requests })

def requests_detail(request, request_id):
    request = Request.objects.get(id=request_id)
    return render(request, 'requests/detail.html', { 'request': request })

# Referenced from http://zetcode.com/django/httprequest/
def data(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']

    msg = f'''
        <html>
        Path: {path}<br>
        Scheme: {scheme}<br>
        Method: {method}<br>
        Address: {address}<br>
        User agent: {user_agent}<br>
        </html>
    '''
    return HttpResponse(msg, content_type='text/html', charset='utf-8')