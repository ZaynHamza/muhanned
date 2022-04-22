from django.urls import path

from . import views

app_name = 'behind_the_scenes'
urlpatterns = [
    path('', views.behind_the_scenes_view, name='behind_the_scenes'),
    path('<int:id>/', views.detail_view, name='detail')
]