from django.urls import path
from posts import views as crud

urlpatterns = [
    #Post CRUD
    path('post/create', crud.PostCreateAPIView),
    path('post/list', crud.PostListAPIView),
    path('post/update/<int:pk>', crud.PostUpdateView),
    path('post/delete/<int:pk>', crud.PostDestroyAPIView),

    # COMMENT CRUD
    path('post/<int:pk1>/create_comment', crud.CommentCreateAPIView),
    path('post/<int:pk1>/comment_list', crud.CommentListAPIView),
    path('post/<int:pk1>/comment_update/<int:pk2>', crud.CommentUpdateView),
    path('post/<int:pk1>/comment_delete/<int:pk2>', crud.CommentDestroyAPIView),

]