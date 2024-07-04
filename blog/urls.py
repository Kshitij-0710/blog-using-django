from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, RegisterView, LoginView, UserDetailsView, LikeView, UnlikeView
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('user/', UserDetailsView.as_view(), name='user_details'),  # Endpoint to fetch user details
    path('posts/<int:pk>/like/', LikeView.as_view(), name='post_like'),
    path('posts/<int:pk>/unlike/', UnlikeView.as_view(), name='post_unlike'),
]
