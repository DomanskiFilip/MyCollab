from collabs.models import Collab

def active_collabs(request):
    return {'active_collabs_count': Collab.objects.filter(active=True).count()}