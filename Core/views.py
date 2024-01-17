from django.shortcuts import render
from collabs.models import Collab, CollabTag
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


def home(request):
    active_collabs = Collab.objects.filter(active=True)
    return render(
        request,
        'Core/index.html',
        {'collabs': active_collabs}
    )
    


def logout_view(request):
    logout(request)
    return redirect('Core:index')

@login_required
def account(request):

    user = request.user
    # collabs = Collab.objects.get(user=user)
    collabs = Collab.objects.all()
    context = {
        'user': user,
        'collabs' : collabs
    }

    return render(request, 'core/account.html', context)

