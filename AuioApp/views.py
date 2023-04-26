# Django views that handle requests from the user interface and perform the appropriate digital signal processing tasks
#from django.shortcuts import render
#from django.http import HttpResponseRedirect
#from .forms import AudioFileForm
from .models import AudioFile
'''
def upload(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            audiofile = AudioFile(audio_file=request.FILES['audio_file'])
            audiofile.save()
            return HttpResponseRedirect('/')
    else:
        form = AudioFileForm()
    return render(request, 'audiofile_form.html', {'form': form})
'''

from django.views.generic.edit import CreateView  # CreateView class, Automatically generates a form for creating new AudioFile instances
from django.urls import reverse_lazy


class AudioFileCreateView(CreateView):
    model = AudioFile
    fields = [
        'name', 'audio_file'
    ]  #fields attribute specifies which fields should be included in the form
    success_url = reverse_lazy(
        'home'
    )  # attribute specifies where to redirect the user after a successful form submission


from django.views.generic import ListView  # class to display a list of AudioFile instances

#         displays a list of uploaded audio files.


class AudioFileListView(ListView):
    model = AudioFile
    template_name = 'audio_file_list.html'  # attribute specifies the template to use for rendering the view
    context_object_name = 'audio_files'  # attribute specifies the variable name to use for the list of AudioFile instances in the template


from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import AudioFileForm


def audio_file_create(request):
    if request.method == 'POST':
        form = AudioFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
    else:
        form = AudioFileForm()
    return render(request, 'audio_file_create.html', {'form': form})
