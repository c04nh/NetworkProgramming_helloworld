from django.template.context_processors import static
from django.urls import path

from helloworld import settings
from musical import views

app_name = 'musical'

urlpatterns = [
    path('frida/', views.frida),
    path('lizzie/', views.lizzie),
]