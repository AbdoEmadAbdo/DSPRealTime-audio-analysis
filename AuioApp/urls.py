from django.urls import path
from .views import AudioFileListView, AudioFileCreateView

urlpatterns = [
    # The name attribute is used to name the URLs so they can be referred to in templates using the {% url %} template tag
    path('', AudioFileListView.as_view(),
         name='home'),  #displays a list of uploaded audio files Page
    path('upload/', AudioFileCreateView.as_view(), name='audio_file_create'
         ),  # which displays the form for uploading audio files
]
