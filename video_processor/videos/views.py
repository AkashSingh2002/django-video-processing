from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm
from .tasks import extract_subtitles

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            extract_subtitles.delay(video.id)  # Call Celery task to extract subtitles
            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})
