from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='assets'),
    path('add-assets/', views.add_assets, name='add_assets'),

]
