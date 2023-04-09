from django.urls import path

from .views import Status

urlpatterns = [
    path('', Status.as_view()),
]
