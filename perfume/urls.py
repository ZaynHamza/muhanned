from django.urls import path

from . import views

app_name = 'perfume'
urlpatterns = [
    path('', views.perfume_view, name='perfume'),
    path('<int:id>/', views.detail_view, name='detail')
]