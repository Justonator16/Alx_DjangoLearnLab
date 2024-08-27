from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'my-models', BookViewSet)

urlpatterns = [
    path("", BookList.as_view(), name="book_list"),
    path("api/", include(router.urls)),
]