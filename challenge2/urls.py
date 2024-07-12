
from django.urls import include, path
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("generic-review-view-set",views.ReviewSet,basename="review")
urlpatterns = [
    path("list",views.carListView,name="car_list"),
    path("<int:pk>",views.carDetailView,name="car_detail_view"),
    path("userlist",views.UserListView,name="user_list"),
    path("showrooms",views.ShowroomView.as_view(),name="show_room_view"),
    path("showroom/<int:pk>",views.ShowroomDetails.as_view(),name="show_room_details"),
    path("generic-review",views.ReviewClass.as_view()),
    path("generic-review/<int:pk>",views.ReviewDetailClass.as_view()),
    path("api/",include(router.urls))
    
    
]
