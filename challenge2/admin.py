from django.contrib import admin
from .models import CarList,ShowroomModel,ReviewModel
# Register your models here.
admin.site.register(CarList)
admin.site.register(ShowroomModel)
admin.site.register(ReviewModel)