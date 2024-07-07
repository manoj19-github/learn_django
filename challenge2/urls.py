
from django.urls import path
from . import views

urlpatterns = [
    path("list",views.carListView,name="car_list"),
    path("<int:pk>",views.carDetailView,name="car_detail_view"),
    path("userlist",views.UserListView,name="user_list"),
    path("showrooms",views.ShowroomView.as_view(),name="show_room_view"),
    path("showroom/<int:pk>",views.ShowroomDetails.as_view(),name="show_room_details"),
    
    
]
