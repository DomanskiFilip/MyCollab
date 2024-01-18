from django.shortcuts import render, redirect, get_object_or_404
from .models import Collab, CollabImage
from .forms import CollabForm, CollabImageFormSet

from django.core.exceptions import PermissionDenied

def collab(request, pk):
    collab = Collab.objects.get(pk=pk)
    images = collab.images.all()
    

    
    return render(request, 'collabs/collab.html', {
        'collab' : collab, 'images' : images
    })
    
    

def create_collab(request):
    form = CollabForm(request.POST or None)
    if request.method == 'POST':
        formset = CollabImageFormSet(request.POST, request.FILES)
        if formset.is_valid() and form.is_valid():
            collab = form.save(commit=False)
            collab.user = request.user
            collab.save()
            
            forms_with_image = [form for form in formset if form.cleaned_data.get('image')]
            # mainImgCount = len([form.cleaned_data.get('is_main', False) for form in forms_with_image])
            mainImgCount = len([form for form in forms_with_image if form.cleaned_data.get('is_main', False)])
            print(mainImgCount)
            
            if mainImgCount == 0:
                  forms_with_image[0].instance.is_main = True
                  print('NO IMAGES MARKED AS MAIN')
            elif mainImgCount > 1:
                print('MANY IMAGES MARKED AS MAIN')
            
            for form in forms_with_image:
                collab_image = form.save(commit=False)
                collab_image.collab = collab
                collab_image.save()
                
        else:
            print('There was an error with the form.')
    else:
        formset = CollabImageFormSet(queryset=CollabImage.objects.none())
    return render(request, 'collabs/new.html', {'form': form, 'formset': formset})




def collab_edit(request, collab_id):
    collab = get_object_or_404(Collab, id=collab_id)

    # Check if the Collab belongs to the current user
    if collab.user != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = CollabForm(request.POST, instance=collab)
        formset = CollabImageFormSet(request.POST, request.FILES, instance=collab)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('collab_detail', collab_id=collab.id)
    else:
        form = CollabForm(instance=collab)
        formset = CollabImageFormSet(instance=collab)

    # Calculate the number of additional images the user can add
    additional_images_count = 5 - collab.images.count()

    return render(request, 'collabs/edit.html', {
        'form': form,
        'formset': formset,
        'additional_images_count': additional_images_count,
    })