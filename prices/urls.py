from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('table/', views.table_view, name='table'),
]
