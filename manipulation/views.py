from django.shortcuts import render, get_object_or_404

from .models import Manipulation, ManipulationImage, ManipulationVideo


def manipulation_view(request):
    manipulations = Manipulation.objects.all()
    return render(request, 'manipulation/manipulation.html', {'manipulations': manipulations})


def detail_view(request, id):
    post = get_object_or_404(Manipulation, id=id)
    photos = ManipulationImage.objects.filter(post=post)
    videos = ManipulationVideo.objects.filter(post=post)
    return render(request, 'manipulation/detail.html', {
        'post': post,
        'photos': photos,
        'videos': videos
    })
