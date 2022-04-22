from django.urls import path

from . import views

app_name = 'fashion'
urlpatterns = [
    path('', views.fashion_view, name='fashion'),
    path('<int:id>/', views.detail_view, name='detail')
]