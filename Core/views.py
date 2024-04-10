from django.shortcuts import render
from collabs.models import Collab, CollabTag
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# NOT THIS
# def home(request):
#     active_collabs = Collab.objects.filter(active=True)
#     active_collabs_with_image = []

#     for collab in active_collabs:
#         main_image = None
#         if hasattr(collab, 'collabimage_set'):
#             main_image = collab.collabimage_set.filter(is_main=True).first()
#         else:
#             print('Collab has no images')
#         active_collabs_with_image.append((collab, main_image))
        
#     return render(
#         request,
#         'Core/index.html',
#         {'collabs_withImg': active_collabs_with_image}
#     )


 
# THIS   
def home(request):
    active_collabs = Collab.objects.filter(active=True)
    active_collabs_with_image = []

    for collab in active_collabs:
        main_image = collab.images.filter(is_main=True).first()
        if main_image is None:
            print('Collab has no main image')
        active_collabs_with_image.append((collab, main_image))
        
    return render(
        request,
        'Core/home.html',
        {'collabs_withImg': active_collabs_with_image}
    )


def logout_view(request):
    logout(request)
    return redirect('Core:home')

@login_required
def account(request):

    user = request.user
    collabs = Collab.objects.filter(user=user)
    context = {
        'user': user,
        'collabs' : collabs
    }

    return render(request, 'core/mycollabs.html', context)