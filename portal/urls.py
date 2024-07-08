from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('alumni/', views.alumni_create_view, name='alumni_create'),
    
]