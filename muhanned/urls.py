"""muhanned URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('behind-the-scenes/', include('behind_the_scenes.urls')),
    path('short-films/', include('short_films.urls')),
    path('fashion/', include('fashion.urls')),
    path('monument/', include('monument.urls')),
    path('manipulation/', include('manipulation.urls')),
    path('beauty/', include('beauty.urls')),
    path('products/', include('products.urls')),
    path('perfume/', include('perfume.urls')),
    path('food/', include('food.urls')),
    path('watches/', include('watches.urls')),
    path('', include('homepage.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
