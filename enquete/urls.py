from django.urls import path
from . import views

urlpatterns = [
    # ex: /enquete/
    path("", views.index, name="index"),
    # ex: /enquete/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /enquete/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /enquete/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
