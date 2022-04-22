from django.shortcuts import render, get_object_or_404

from .models import Food, FoodImage, FoodVideo


def food_view(request):
    foods = Food.objects.all()
    return render(request, 'food/food.html', {'foods': foods})


def detail_view(request, id):
    post = get_object_or_404(Food, id=id)
    photos = FoodImage.objects.filter(post=post)
    videos = FoodVideo.objects.filter(post=post)
    return render(request, 'food/detail.html', {
        'post': post,
        'photos': photos,
        'videos': videos
    })
