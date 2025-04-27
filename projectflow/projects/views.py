from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth import get_user_model
from .models import Project, ProjectMember
from .serializers import ProjectSerializer
import secrets

User = get_user_model()

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        project = serializer.save(owner=self.request.user)
        ProjectMember.objects.create(user=self.request.user, project=project, role="admin")

    def retrieve(self, request, *args, **kwargs):
        project = self.get_object()

        # Проверка: является ли пользователь владельцем или участником
        if request.user != project.owner and not project.members.filter(id=request.user.id).exists():
            return Response({'detail': 'У вас нет доступа к этому проекту, вы не являетесь участником.'},
                            status=status.HTTP_403_FORBIDDEN)

        serializer = self.get_serializer(project)
        return Response(serializer.data)

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated], url_path='generate_invite')
    def generate_invite(self, request, pk=None):
        # Получаем проект
        project = self.get_object()

        # Проверяем, что пользователь является владельцем проекта
        if project.owner != request.user:
            return Response({'error': 'Only the owner can generate invite links.'}, status=403)

        # Генерируем токен для приглашения
        invite_token = secrets.token_urlsafe(64)
        project.invite_token = invite_token
        project.save()

        invite_url = f"{request.build_absolute_uri('/api/projects/invite/')}{invite_token}/"
        return Response({'invite_url': invite_url})

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def join_by_token(self, request, token=None):
        try:
            # Ищем проект по токену
            project = Project.objects.get(invite_token=token)
            # Добавляем пользователя в проект
            ProjectMember.objects.get_or_create(user=request.user, project=project)
            return Response({'status': 'Joined project by invite link'})
        except Project.DoesNotExist:
            return Response({'error': 'Invalid invite token'}, status=400)
