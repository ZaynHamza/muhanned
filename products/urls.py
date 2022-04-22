from django.urls import path

from . import views

app_name = 'products'
urlpatterns = [
    path('', views.product_view, name='products'),
    path('<int:id>/', views.detail_view, name='detail')
]