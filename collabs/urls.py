from django.urls import path
from . import views

app_name = 'collabs'

urlpatterns = [
    path('<pk>', views.collab, name='collab'),
    path('new/', views.create_collab, name='new_collab')
]