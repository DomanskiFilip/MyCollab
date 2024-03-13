from django.shortcuts import render, redirect, get_object_or_404
from .models import Collab, CollabImage
from .forms import CollabForm, CollabImageFormSet
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST



def collab(request, pk):
    collab = Collab.objects.get(pk=pk)
    images = CollabImage.objects.filter(collab=collab)
    
    return render(request, 'collabs/collab.html', {
        'collab' : collab, 'images' : images
    })
    
    


@login_required
def create_collab(request):
    form = CollabForm(request.POST or None)
    formset = CollabImageFormSet(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            collab = form.save(commit=False)
            collab.user = request.user
            collab.save()
            form.save_m2m()  # Save the many-to-many data

        if formset.is_valid():
            forms_with_image = [form for form in formset if form.cleaned_data.get('image')]
            mainImgCount = len([form for form in forms_with_image if form.cleaned_data.get('is_main', False)])

            if mainImgCount == 0:
                print('NO IMAGES MARKED AS MAIN')
            elif mainImgCount > 1:
                print('MANY IMAGES MARKED AS MAIN')
                return render(request, 'collabs/new.html', {'form': form, 'formset': formset, 'error': 'Only one image can be marked as main.'})

            for form in formset:
                if form.cleaned_data.get('image') or form.cleaned_data.get('description'):
                    collab_image = form.save(commit=False)
                    collab_image.collab = collab
                    if not forms_with_image and not collab_image.is_main:
                        collab_image.is_main = True
                    collab_image.save()

            # Redirect to the collab detail page of the newly created collab
            return redirect('collabs:collab', pk=collab.id)

        else:
            print('There was an error with the formset.')

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
            forms_with_image = [form for form in formset if form.cleaned_data.get('image')]
            form.save()
            formset.save()
            if form.cleaned_data.get('image') or form.cleaned_data.get('description'):
                    collab_image = form.save(commit=False)
                    collab_image.collab = collab
                    if not forms_with_image and not collab_image.is_main:
                        collab_image.is_main = True
                    collab_image.save()
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



@require_POST
@login_required
def collab_delete(request, pk):
    collab = get_object_or_404(Collab, pk=pk)
    if request.method == 'POST':
        collab.delete()
        return redirect('Core:index') 