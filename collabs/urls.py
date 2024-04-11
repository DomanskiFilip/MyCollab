from django.urls import path
from . import views

app_name = 'collabs'

urlpatterns = [
    path('new/', views.create_collab, name='new_collab'),
    path('<pk>', views.collab, name='collab'),
    path('edit/<collab_id>', views.collab_edit, name='edit'),
    path('delete_image/', views.delete_image, name='delete_image'),
    path('<int:pk>/delete/', views.collab_delete, name='delete'),
    path('<int:pk>/deleteR/', views.collab_delete_reload, name='deleteR'),
]

