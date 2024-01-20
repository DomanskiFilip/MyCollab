from django.shortcuts import render, redirect, get_object_or_404
from .models import Collab, CollabImage
from .forms import CollabForm, CollabImageFormSet

from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required



def collab(request, pk):
    collab = Collab.objects.get(pk=pk)
    images = CollabImage.objects.filter(collab=collab)
    
    return render(request, 'collabs/collab.html', {
        'collab' : collab, 'images' : images
    })
    
    
@login_required
def create_collab(request):
    form = CollabForm(request.POST or None)
    if request.method == 'POST':
        formset = CollabImageFormSet(request.POST, request.FILES)
        if formset.is_valid() and form.is_valid():
            collab = form.save(commit=False)
            collab.user = request.user
            collab.save()
            form.save_m2m()  # Save the many-to-many data

            forms_with_image = [form for form in formset if form.cleaned_data.get('image')]
            mainImgCount = len([form for form in forms_with_image if form.cleaned_data.get('is_main', False)])

            if mainImgCount == 0:
                forms_with_image[0].instance.is_main = True
                print('NO IMAGES MARKED AS MAIN')
            elif mainImgCount > 1:
                print('MANY IMAGES MARKED AS MAIN')
                return render(request, 'collabs/new.html', {'form': form, 'formset': formset, 'error': 'Only one image can be marked as main.'})

            for form in forms_with_image:
                collab_image = form.save(commit=False)
                collab_image.collab = collab
                collab_image.save()

        else:
            print('There was an error with the form.')
    else:
        formset = CollabImageFormSet(queryset=CollabImage.objects.none())
    return render(request, 'collabs/new.html', {'form': form, 'formset': formset})


@login_required
def collab_edit(request, collab_id):
    collab = get_object_or_404(Collab, id=collab_id)

    if collab.user != request.user:
        raise PermissionDenied

    if request.method == 'POST':
        form = CollabForm(request.POST, instance=collab)
        formset = CollabImageFormSet(request.POST, request.FILES, instance=collab)

        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('collabs:collab', pk=collab.id)
    else:
        form = CollabForm(instance=collab)
        if collab.images.exists():
            formset = CollabImageFormSet(instance=collab)
        else:
            formset = CollabImageFormSet(queryset=CollabImage.objects.none())

    additional_images_count = 5 - collab.images.count()

    return render(request, 'collabs/edit.html', {
        'form': form,
        'formset': formset,
        'additional_images_count': additional_images_count,
    })

@login_required 
def delete_image(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image = CollabImage.objects.get(id=image_id)
        image.delete()
    return redirect('collabs:edit', collab_id=image.collab.pk)