from django.urls import path
from rest_framework import routers
from .views import CategoryView,BrandView


router = routers.DefaultRouter()
router.register("categories", CategoryView)
router.register("brand", BrandView)


urlpatterns = [
    
] + router.urls
