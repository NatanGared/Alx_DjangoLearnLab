# urls.py
from django.urls import path
from .views import (
    HomeView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    register, user_login, user_logout, profile,
    PostDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('post/', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:post_pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('post/<int:post_pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),  # Create a new comment
    path('comments/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),  # Edit a comment
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),  # Delete a comment
]