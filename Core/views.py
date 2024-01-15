from django.shortcuts import render
from collabs.models import Collab, CollabTag

def home(request):
    active_collabs = Collab.objects.filter(active=True)
    return render(
        request,
        'Core/index.html',
        {'collabs': active_collabs}
    )
    
    