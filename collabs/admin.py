from django.contrib import admin
from .models import Collab, CollabTag, CollabImage


from django.contrib import admin
from django.core.exceptions import PermissionDenied
from django.contrib.admin.actions import delete_selected as delete_selected_

def delete_selected(modeladmin, request, queryset):
    if not modeladmin.has_delete_permission(request):
        raise PermissionDenied
    for obj in queryset:
        obj.delete()
delete_selected.short_description = delete_selected_.short_description

class CollabAdmin(admin.ModelAdmin):
    actions = [delete_selected]

admin.site.register(Collab, CollabAdmin)


admin.site.register(CollabTag)
admin.site.register(CollabImage)