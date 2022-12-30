from django.contrib import admin
from django.urls import path, include
from app.views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'core', AppViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), 
]
