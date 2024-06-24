from django.urls import path
from .views import home, create



urlpatterns = [
    path('', home, name='home'),
    path('create', create, name='create'),
]