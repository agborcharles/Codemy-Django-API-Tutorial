from django.urls import path, include
from . import views
from rest_framework import routers

# create a variable for the router
router = routers.DefaultRouter()
router.register('Courses', views.CourseView)



urlpatterns = [
    path('',include(router.urls)),

]
