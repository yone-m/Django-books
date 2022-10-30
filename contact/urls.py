from django.urls import path, include
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.Top.as_view(), name='top'),
    path('thanks/', views.Thanks.as_view(), name='thanks')
]
