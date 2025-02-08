# views.py
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import APIEndpoint

def index(request):
    endpoints = APIEndpoint.objects.all()
    total = endpoints.count()
    completed = endpoints.filter(completed=True).count()
    progress = (completed / total * 100) if total > 0 else 0
    return render(request, 'index.html', {'endpoints': endpoints, 'progress': progress, 'remaining': total - completed})

def update_status(request, endpoint_id):
    endpoint = get_object_or_404(APIEndpoint, id=endpoint_id)
    endpoint.completed = not endpoint.completed
    endpoint.save()
    return JsonResponse({'success': True})