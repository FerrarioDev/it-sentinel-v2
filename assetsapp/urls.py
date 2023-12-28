from django.urls import path
from . import views
from .views import Add_assets, AssetListView

urlpatterns = [
    path('', views.index, name='assets'),
    path('add-assets/', Add_assets.as_view(), name='add_assets'),
    path('list/<str:category>/', AssetListView.as_view(), name='asset_list'),

]
