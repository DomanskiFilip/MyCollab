from django import forms
from .models import Collab, CollabImage

class CollabForm(forms.ModelForm):
    class Meta:
        model = Collab
        fields = ('title', 'description', 'tags')  # replace with your actual fields


# class CollabImageForm(forms.ModelForm):
#     is_main = forms.BooleanField(required=False, widget=forms.RadioSelect)
#     class Meta:
#         model = CollabImage
#         fields = ('image', 'is_main',)

CollabImageFormSet = forms.modelformset_factory(CollabImage, fields=('image', 'is_main'), extra=5, max_num=5)