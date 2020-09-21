from django.urls import path
from . import views

urlpatterns = [
    path('', views.requests_index, name='index'),
    path('about/', views.about, name='about'),
    path('requests/', views.requests_index, name='index'),
    path('requests/<int:request_id>/', views.requests_detail, name='detail'),
    path('requests/create/', views.RequestCreate.as_view(), name='requests_create'),
]