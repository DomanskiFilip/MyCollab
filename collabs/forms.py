from django import forms
from .models import Collab, CollabImage

class CollabForm(forms.ModelForm):
    class Meta:
        model = Collab
        fields = ('title', 'tags', 'introduction')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input_title'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox_tags'}),
            'introduction': forms.Textarea(attrs={'class': 'textarea_description'}),
        }

# https://www.letscodemore.com/blog/django-inline-formset-factory-with-examples/

class CollabImageForm(forms.ModelForm):
    class Meta:
        model = CollabImage
        fields = ('image', 'is_main', 'description')
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'input_image'}),
            'is_main': forms.CheckboxInput(attrs={'class': 'checkbox_is_main'}),
            'description': forms.Textarea(attrs={'class': 'textarea_description'}),
        }

CollabImageFormSet = forms.inlineformset_factory(Collab, CollabImage, form=CollabImageForm, extra=3, max_num=3, can_delete=True, can_delete_extra=False)