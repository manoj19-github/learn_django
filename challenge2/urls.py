
from django.urls import path
from . import views

urlpatterns = [
    path("list",views.carListView,name="car_list"),
    path("<int:pk>",views.carDetailView,name="car_detail_view"),
    path("userlist",views.UserListView,name="user_list")
    
    
]
