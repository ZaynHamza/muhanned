from django.shortcuts import render, get_object_or_404

from .models import Monument,MonumentImage, MonumentVideo


def monument_view(request):
    monuments = Monument.objects.all()
    return render(request, 'monument/monument.html', {'monuments': monuments})


def detail_view(request, id):
    post = get_object_or_404(Monument, id=id)
    photos = MonumentImage.objects.filter(post=post)
    videos = MonumentVideo.objects.filter(post=post)
    return render(request, 'monument/detail.html', {
        'post': post,
        'photos': photos,
        'videos': videos
    })
