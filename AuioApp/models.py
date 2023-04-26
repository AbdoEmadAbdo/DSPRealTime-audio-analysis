from django.db import models


class AudioFile(models.Model):  # store the uploaded audio files
    name = models.CharField(max_length=100) # store the name of the audio file
    audio_file = models.FileField(upload_to='audio/')

    processed_file = models.FileField(upload_to='processed_audio/',
                                      blank=True,
                                      null=True)  #processing
    processed = models.BooleanField(default=False)  # done
    created_at = models.DateTimeField(auto_now_add=True) # timestamp to record when the file was uploaded.
