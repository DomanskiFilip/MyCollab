from django import forms
from .models import Collab, CollabImage

class CollabForm(forms.ModelForm):
    class Meta:
        model = Collab
        fields = ('title', 'description', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input_title'}),
            'description': forms.Textarea(attrs={'class': 'textarea_description'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox_tags'}),
        }

# https://www.letscodemore.com/blog/django-inline-formset-factory-with-examples/

class CollabImageForm(forms.ModelForm):
    class Meta:
        model = CollabImage
        fields = ('image', 'is_main')
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'input_image'}),
            'is_main': forms.CheckboxInput(attrs={'class': 'checkbox_is_main'}),
        }

CollabImageFormSet = forms.inlineformset_factory(Collab, CollabImage, form=CollabImageForm, extra=5, max_num=5, can_delete=True, can_delete_extra=False)