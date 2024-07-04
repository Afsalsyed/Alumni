from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('alumni_form/', views.alumni_form_view, name='alumni_form'),
]