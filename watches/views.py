from django.shortcuts import render, get_object_or_404

from .models import Watch, WatchImage, WatchVideo


def watch_view(request):
    watches = Watch.objects.all()
    return render(request, 'watches/watches.html', {'watches': watches})


def detail_view(request, id):
    post = get_object_or_404(Watch, id=id)
    photos = WatchImage.objects.filter(post=post)
    videos = WatchVideo.objects.filter(post=post)
    return render(request, 'watches/detail.html', {
        'post': post,
        'photos': photos,
        'videos': videos
    })
