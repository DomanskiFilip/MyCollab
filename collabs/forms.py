from django import forms
from .models import Collab, CollabImage, CollabTag
from django.utils.html import format_html, escape
from django.utils.safestring import mark_safe

class CollabFilterForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        queryset=CollabTag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

class CollabForm(forms.ModelForm):
    class Meta:
        model = Collab
        fields = ('title', 'tags', 'introduction')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'input_title'}),
            'tags': forms.CheckboxSelectMultiple(attrs={'class': 'checkbox_tags'}),
            'introduction': forms.Textarea(attrs={'class': 'textarea_description'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = False
        self.fields['introduction'].required = False

class CustomClearableFileInput(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        attrs = attrs or {}
        attrs['class'] = 'input_image'
        custom_html = super().render(name, value, attrs, renderer)


        if value and hasattr(value, "url"):
            Change_text = "Change: "
            checkbox_label = "Clear: "
            checkbox_name = self.clear_checkbox_name(name)
            checkbox_id = self.clear_checkbox_id(checkbox_name)

            file_number = ''.join(filter(str.isdigit, name))
            change_name = f'images-{file_number}-image'
            change_id = f'id_images-{file_number}-image'

            clear_checkbox = ''
            if not self.is_required:
                clear_checkbox = format_html(
                    '<label for="{}" class="formImgLabel">{}</label>' \
                    '<input type="checkbox" name="{}" id="{}" />',
                    checkbox_id, checkbox_label, checkbox_name, checkbox_id
                )

            file_input_html = format_html(
                '<label for="{}" class="formImgLabel">{}</label>' \
                '<input type="file" name="{}" class="input_image" accept="image/*" id="{}">',
                change_id, Change_text, change_name, change_id
            )
            custom_html = format_html('{}{}', file_input_html, clear_checkbox)
        else:
            custom_html = format_html('<span></span>{}', custom_html)

        return mark_safe(custom_html)


class CollabImageForm(forms.ModelForm):
    class Meta:
        model = CollabImage
        fields = ('image', 'is_main', 'description')
        widgets = {
            'description': forms.Textarea(attrs={'class': 'textarea_description'}),
            'image': CustomClearableFileInput(attrs={'class': 'input_image'}),
            'is_main': forms.CheckboxInput(attrs={'class': 'checkbox_is_main'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['description'].required = False

CollabImageFormSet = forms.inlineformset_factory(Collab, CollabImage, form=CollabImageForm, extra=3, max_num=3, can_delete=True, can_delete_extra=False)



    
