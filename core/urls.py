from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('food/<int:pk>/', views.detail_view.as_view(), name='detail'),
    path('additem/', views.CreateItem.as_view(), name='create_item'),
    path('updateitem/<int:id>/', views.update_item, name='update_item'),
    path('deleteitem/<int:id>/', views.delete_item, name='delete_item')
]
