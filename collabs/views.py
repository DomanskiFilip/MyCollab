from django.shortcuts import render, redirect, get_object_or_404
from .models import Collab, CollabImage, CollabTag
from .forms import CollabForm, CollabImageFormSet, CollabFilterForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from .forms import CollabForm, CollabImageFormSet
from .models import Collab, CollabImage
from .wordFilter import filter_bad_words
from django.contrib import messages
from django.db.models import Q, Count
from django.http import JsonResponse
from django.conf import settings
from django.utils.dateformat import DateFormat
from django.utils.formats import get_format

def collab_list(request):
    selected_tags = request.GET.getlist('tags')
    search_query = request.GET.get('search', '')
    base_query = Collab.objects.all()

    if selected_tags and search_query:
        base_query = Collab.objects.filter(
            Q(title__icontains=search_query) | 
            Q(title__iregex=r'\b{}\b'.format(search_query)),
            tags__name__in=selected_tags
        ).distinct().annotate(matched_tags_count=Count('tags', filter=Q(tags__name__in=selected_tags))).filter(matched_tags_count=len(selected_tags))
    elif selected_tags:
        base_query = Collab.objects.filter(tags__name__in=selected_tags).distinct()
        base_query = base_query.annotate(matched_tags_count=Count('tags', filter=Q(tags__name__in=selected_tags)))
        base_query = base_query.filter(matched_tags_count=len(selected_tags))
    elif search_query:
        base_query = Collab.objects.filter(
            Q(title__icontains=search_query) | 
            Q(title__iregex=r'\b{}\b'.format(search_query))
        ).distinct()
    else:
        base_query = Collab.objects.all()

    collabs_withImg = base_query.distinct()

    collabs_withImg_list = []
    for collab in collabs_withImg:
        readable_date = DateFormat(collab.created_at).format(get_format('DATE_FORMAT'))

        # Filter for the main image
        main_image = collab.images.filter(is_main=True).first()
        main_image_url = request.build_absolute_uri(settings.MEDIA_URL + main_image.image.name) if main_image else None

        # Get tags
        tags = [tag.name for tag in collab.tags.all()]

        collab_dict = {
            "pk": collab.pk,
            "title": collab.title,
            "introduction": "" if main_image else collab.introduction,
            "main_image": {"src": main_image_url} if main_image_url else "",
            "tags": tags,
            "created_at": readable_date,
        }
        collabs_withImg_list.append(collab_dict)
    return JsonResponse({'collabs_withImg': collabs_withImg_list})

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
    collab = None

    if request.method == 'POST':
        if form.is_valid():
            collab = form.save(commit=False)
            collab.title = filter_bad_words(collab.title)
            collab.introduction = filter_bad_words(collab.introduction)
            collab.user = request.user
            collab.save()
            form.save_m2m()  

        if formset.is_valid():
            forms_with_image = [form for form in formset if form.cleaned_data.get('image')]
            
            for form in formset:
                if form.cleaned_data.get('image') or form.cleaned_data.get('description'):
                    collab_image = form.save(commit=False)
                    collab_image.collab = collab
                    if not forms_with_image and not collab_image.is_main:
                        collab_image.is_main = True
                    collab_image.save()

        else:
            print('There was an error with the formset.')

        if collab is not None:
            # Redirect to the collab detail page of the newly created collab
            return redirect('collabs:collab', pk=collab.id)

    else:
        formset = CollabImageFormSet(queryset=CollabImage.objects.none())

    return render(request, 'collabs/new.html', {'form': form, 'formset': formset})

@login_required
def collab_edit(request, pk):
    collab = get_object_or_404(Collab, id=pk)
    if request.method == 'POST':
        form = CollabForm(request.POST, instance=collab)
        formset = CollabImageFormSet(request.POST, request.FILES, instance=collab)
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            messages.success(request, 'Collab and images updated successfully.')
            return redirect('collabs:collab', pk=collab.id)
        else:
            # If form or formset is not valid, add an error message
            messages.error(request, 'Error updating collab. Please check the form for errors.')
  
    else:
        form = CollabForm(instance=collab)
        formset = CollabImageFormSet(instance=collab)

    if not form.is_valid() or not formset.is_valid():
            print("Form errors:", form.errors)
            print("Formset errors:", formset.errors)

    return render(request, 'collabs/edit.html', {'form': form, 'formset': formset})

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
        return redirect('Core:home') 
    
@require_POST
@login_required
def collab_delete_reload(request, pk):
    collab = get_object_or_404(Collab, pk=pk)
    if request.method == 'POST':
        collab.delete()
        return redirect('Core:mycollabs') 