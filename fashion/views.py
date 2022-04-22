from django.shortcuts import render, get_object_or_404

from .models import Fashion, FashionImage, FashionVideo


def fashion_view(request):
    fashions = Fashion.objects.all()
    return render(request, 'fashion/fashion.html', {'fashions': fashions})


def detail_view(request, id):
    post = get_object_or_404(Fashion, id=id)
    photos = FashionImage.objects.filter(post=post)
    videos = FashionVideo.objects.filter(post=post)
    return render(request, 'fashion/detail.html', {
        'post': post,
        'photos': photos,
        'videos': videos
    })
