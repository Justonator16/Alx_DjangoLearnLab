from django.urls import path, include
from .views import BookList, BookViewSet, CustomAuthToken, BookCreateAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'my-models', BookViewSet)

urlpatterns = [
    path("", BookList.as_view(), name="book_list"),
    path("api/", include(router.urls)),
    path('api-token-auth', CustomAuthToken.as_view(), name='api_token_auth'),
    path("books/", BookCreateAPIView.as_view(), name="books-list-create"),

]