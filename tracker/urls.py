from django.urls import path
from . import views
from .views import index, update_status

urlpatterns = [
    path('', views.index, name='index'),
    path('update-status/<int:endpoint_id>/', update_status, name='update_status'),
]
