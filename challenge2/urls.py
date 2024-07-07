
from django.urls import path
from . import views

urlpatterns = [
    # path("january",views.index),
    # # dynamic path
    # path("<month>",views.monthSwitch)
    path("list",views.carListView,name="car_list"),
    path("<int:pk>",views.carDetailView,name="car_detail_view")
    
    
]
