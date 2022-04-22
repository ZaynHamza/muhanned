from django.urls import path

from . import views

app_name = 'beauty'
urlpatterns = [
    path('', views.beauty_view, name='beauty'),
    path('<int:id>/', views.detail_view, name='detail')
]