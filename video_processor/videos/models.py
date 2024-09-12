from django.db import models

class Video(models.Model):
    video_file = models.FileField(upload_to='videos/')
    subtitle_file = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
