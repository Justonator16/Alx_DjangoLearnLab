from django.urls import path
from .views import list_books, LibraryDetailView ,LibraryListView ,BookView

urlpatterns = [
    path("", list_books, name="books"),
    path("library/", BookView.as_view(), name="library"),
    path("library_detail/", LibraryDetailView.as_view(), name="library_detail"),
    path("library_list/", LibraryListView.as_view(), name="library_list"),
]