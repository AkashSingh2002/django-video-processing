import subprocess
from celery import shared_task
from .models import Video

@shared_task
def extract_subtitles(video_id):
    video = Video.objects.get(id=video_id)
    video_path = video.video_file.path
    subtitle_path = f"{video_path}.srt"

    # Run ffmpeg command to extract subtitles
    subprocess.run([
        "ffmpeg", 
        "-i", video_path,
        "-map", "0:s:0",
        subtitle_path
    ])

    with open(subtitle_path, 'r') as subtitle_file:
        video.subtitle_file = subtitle_file.read()
        video.save()
