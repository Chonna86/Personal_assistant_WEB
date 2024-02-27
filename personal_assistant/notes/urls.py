from django.urls import path
from .views import note_list, add_note, edit_note, delete_note, add_tag

app_name = 'notes'
urlpatterns = [
    path("", note_list, name='note_list'),
    path("add/", add_note, name='add_note'),
    path("edit/<int:note_id>/", edit_note, name='edit_note'),
    path("delete/<int:note_id>/", delete_note, name='delete_note'),
    path("add_tag/", add_tag, name='add_tag'),
]