from django.urls import path, include
from .import views 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Details', views.DetailsView) 

urlpatterns = [
    path('', include(router.urls)),

]