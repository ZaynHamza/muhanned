from django.urls import path

from . import views

app_name = 'manipulation'
urlpatterns = [
    path('', views.manipulation_view, name='manipulation'),
    path('<int:id>/', views.detail_view, name='detail')
]