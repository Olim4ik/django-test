from django.urls import path

from . import views

urlpatterns = [
    path("list/", views.PollListView.as_view()),
    path("detail/<int:pk>/", views.PollDetailView.as_view()),
    path("create/", views.PollCreateView.as_view()),
    path("update/<int:pk>/", views.PollUpdateView.as_view()),
    path("delete/<int:pk>/", views.PollDeleteView.as_view()),
]
