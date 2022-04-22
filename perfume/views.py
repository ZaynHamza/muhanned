from django.shortcuts import render, get_object_or_404

from .models import Perfume, PerfumeImage, PerfumeVideo


def perfume_view(request):
    perfumes = Perfume.objects.all()
    return render(request, 'perfume/perfume.html', {'perfumes': perfumes})


def detail_view(request, id):
    post = get_object_or_404(Perfume, id=id)
    photos = PerfumeImage.objects.filter(post=post)
    videos = PerfumeVideo.objects.filter(post=post)
    return render(request, 'perfume/detail.html', {
        'post': post,
        'photos': photos,
        'videos': videos
    })
