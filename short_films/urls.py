from django.urls import path

from . import views

app_name = 'short_films'
urlpatterns = [
    path('', views.short_films_view, name='short_films'),
    path('<int:id>/', views.detail_view, name='detail')
]