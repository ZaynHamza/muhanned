from django.shortcuts import render, get_object_or_404

from .models import BehindTheScenes, BehindTheScenesImage, BehindTheScenesVideo


def behind_the_scenes_view(request):
    behind_the_scenes = BehindTheScenes.objects.all()
    return render(request, 'behind_the_scenes/behind_the_scenes.html', {'behind_the_scenes': behind_the_scenes})


def detail_view(request, id):
    post = get_object_or_404(BehindTheScenes, id=id)
    photos = BehindTheScenesImage.objects.filter(post=post)
    videos = BehindTheScenesVideo.objects.filter(post=post)
    return render(request, 'behind_the_scenes/detail.html', {
        'post': post,
        'photos': photos,
        'videos': videos
    })
