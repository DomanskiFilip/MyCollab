from django.shortcuts import render
from collabs.models import Collab

# Create your views here.

def collab(request, pk):
    collab = Collab.objects.get(pk=pk)

    
    return render(request, 'collabs/collab.html', {
        'collab' : collab,
    })
    
    
    

