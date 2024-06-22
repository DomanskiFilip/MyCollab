from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'collabs'

urlpatterns = [
    path('collab_list/', views.collab_list, name='collab_list'),
    path('new/', views.create_collab, name='new_collab'),
    path('<pk>', views.collab, name='collab'),
    path('edit/<int:pk>', views.collab_edit, name='edit'),
    path('delete_image/', views.delete_image, name='delete_image'),
    path('<int:pk>/delete/', views.collab_delete, name='delete'),
    path('<int:pk>/deleteR/', views.collab_delete_reload, name='deleteR'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

