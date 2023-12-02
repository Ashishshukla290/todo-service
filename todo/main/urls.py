from django.urls import path, include
from django.contrib import admin
from .views import Todoviewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"todo", Todoviewset, basename="todo")

urlpatterns = [
    path("", include(router.urls)),
    path("readall/", Todoviewset.as_view({"get": "readall"}), name="read-all"),
    path(
        "readtask/<int:id>/", Todoviewset.as_view({"get": "readtask"}), name="read-task"
    ),
    path(
        "changetask/<int:id>/", Todoviewset.as_view({"patch": "change"}), name="change"
    ),
    path(
        "delete/<int:id>/", Todoviewset.as_view({"delete": "destroy"}), name="destroy"
    ),
]
