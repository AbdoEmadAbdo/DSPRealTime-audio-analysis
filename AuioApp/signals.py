# Add a signal to process the uploaded audio file
#Using "Django signals" --->  to process the uploaded audio file as soon as it saved. using a library (pydub or librosa) to perform DSP processing and analysis.

# when an AudioFile instance is saved

from django.db.models.signals import post_save  # post_save --> signal is used to detect when an AudioFile instance is saved
from django.dispatch import receiver
from .models import AudioFile
from pydub import AudioSegment


@receiver(post_save, sender=AudioFile)  # decorator used to register the process_audio function as the receiver for this signal
#function checks if the processed field of the AudioFile instance is False, indicating that the file has not yet been processed. It then loads the audio file using pydub, reverses it, and saves the processed file to the processed_file field of the AudioFile instance.

def process_audio(sender, instance, **kwargs):
    if not instance.processed:
        audio_file = instance.audio_file.path
        processed_file = instance.processed_file.path
        sound = AudioSegment.from_file(audio_file, format="mp3")
        sound.reverse()


