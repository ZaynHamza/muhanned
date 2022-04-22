from django.shortcuts import render, get_object_or_404

from .models import Beauty, BeautyImage, BeautyVideo


def beauty_view(request):
    beauties = Beauty.objects.all()
    return render(request, 'beauty/beauty.html', {'beauties': beauties})


def detail_view(request, id):
    post = get_object_or_404(Beauty, id=id)
    photos = BeautyImage.objects.filter(post=post)
    videos = BeautyVideo.objects.filter(post=post)
    return render(request, 'beauty/detail.html', {
        'post': post,
        'photos': photos,
        'videos': videos
    })
