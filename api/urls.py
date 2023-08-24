from django.urls import path, include

urlpatterns = [
    path("poll/", include("api.poll.urls"))
]