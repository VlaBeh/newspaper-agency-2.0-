from django.urls import path
from catalog.views import *
urlpatterns = [
    path("", index, name="index"),
    path("topic/", TopicFormatListView.as_view(), name="topic-list"),
    path("topic/create/", TopicFormatCreateView.as_view(), name="topic-form"),
    path("topic/<int:pk>/update/", TopicFormatUpdateView.as_view(), name="topic-update"),
    path("topic/<int:pk>/delete/", TopicFormatDeleteView.as_view(), name="topic-delete"),
    path("newspapers", NewspaperFormatListView.as_view(), name="newspaper-list"),
    path("newspapers/create/", NewspaperFormatCreateView.as_view(), name="newspaper-form"),
    path("newspapers/<int:pk>/update", NewspaperFormatUpdateView.as_view(), name="newspaper-update"),
    path("newspapers/<int:pk>/delete", NewspaperFormatDeleteView.as_view(), name="newspaper-delete"),
    path("newspapers/<int:pk>/", NewspaperFormatDetailView.as_view(), name="newspaper-detail"),
    path("redactors", RedactorFormatListView.as_view(), name="redactor-list"),
    path("redactors/create/", RedactorFormatCreateView.as_view(), name="redactor-form"),
    path("redactors/<int:pk>/", RedactorFormatDetailView.as_view(), name="redactor_detail"),
]


app_name = "catalog"
