from django.urls import path
from LiveData_App import views

urlpatterns = [
    path('', views.sample, name='sample'),
    path('view_about', views.view_about, name='view_about'),
    
]