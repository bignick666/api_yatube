from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views

from api.views import PostViewSet, GroupViewSet,\
    CommentViewSet

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(
    r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)',
    CommentViewSet, basename='comment_detail'
)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),

]
