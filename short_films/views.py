from django.shortcuts import render, get_object_or_404

from .models import ShortFilms, ShortFilmsImage, ShortFilmsVideo


def short_films_view(request):
    short_films = ShortFilms.objects.all()
    return render(request, 'short_films/short_films.html', {'short_films': short_films})


def detail_view(request, id):
    post = get_object_or_404(ShortFilms, id=id)
    photos = ShortFilmsImage.objects.filter(post=post)
    videos = ShortFilmsVideo.objects.filter(post=post)
    return render(request, 'short_films/detail.html', {
        'post': post,
        'photos': photos,
        'videos': videos
    })
