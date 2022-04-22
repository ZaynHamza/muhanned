from django.urls import path

from . import views

app_name = 'food'
urlpatterns = [
    path('', views.food_view, name='food'),
    path('<int:id>/', views.detail_view, name='detail')
]
