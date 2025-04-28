from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('<int:pk>/generate_invite/', ProjectViewSet.as_view({'get': 'generate_invite'}), name='project-generate-invite'),
    path('invite/<str:token>/', ProjectViewSet.as_view({'get': 'join_by_token'}), name='project-join-by-token'),
]
# path('join_by_token/<str:token>/', ProjectViewSet.as_view({'get': 'join_by_token'}), name='project-join-by-token'),
