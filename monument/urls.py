from django.urls import path

from . import views

app_name = 'monument'
urlpatterns = [
    path('', views.monument_view, name='monument'),
    path('<int:id>/', views.detail_view, name='detail')
]