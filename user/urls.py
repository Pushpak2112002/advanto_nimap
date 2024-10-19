from django.contrib import admin
from django.urls import path,include
from user.views import compnyViewset
from user.views import clientsViewset
from user.views import projectViewset
from rest_framework import routers

router= routers.DefaultRouter()
router.register(r'user', compnyViewset)


router= routers.DefaultRouter()
router.register(r'clients', clientsViewset)


router= routers.DefaultRouter()
router.register(r'project', projectViewset)

urlpatterns = [
    path('',include(router.urls)),
]