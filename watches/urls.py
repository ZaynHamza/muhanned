from django.urls import path

from . import views

app_name = 'watches'
urlpatterns = [
    path('', views.watch_view, name='watch'),
    path('<int:id>/', views.detail_view, name='detail')
]
