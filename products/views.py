from django.shortcuts import render, get_object_or_404

from .models import Product, ProductImage, ProductVideo


def product_view(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def detail_view(request, id):
    post = get_object_or_404(Product, id=id)
    photos = ProductImage.objects.filter(post=post)
    videos = ProductVideo.objects.filter(post=post)
    return render(request, 'products/detail.html', {
        'post': post,
        'photos': photos,
        'videos': videos
    })
