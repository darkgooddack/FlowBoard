from projects.models import ProjectMember
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.db import models
from django.db.models import Q


from .models import Task
from .serializers import TaskSerializer, TaskCommentSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    swagger_tags = ['Tasks']

    def perform_create(self, serializer):
        project = serializer.validated_data['project']
        if not ProjectMember.objects.filter(project=project, user=self.request.user).exists():
            raise PermissionError('Вы не участник проекта.')
        serializer.save(created_by=self.request.user)

    # GET /api/tasks/?project=1
    def get_queryset(self):
        user = self.request.user
        queryset = Task.objects.filter(
            models.Q(created_by=user) | models.Q(assignees=user)
        ).distinct()  # чтобы убрать дубликаты, если совпадают created_by и assignees

        project_id = self.request.query_params.get('project')
        if project_id:
            if not ProjectMember.objects.filter(project_id=project_id, user=user).exists():
                # Если не участник проекта — вообще ничего не показываем
                return Task.objects.none()
            queryset = queryset.filter(project_id=project_id)

        return queryset

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def comments_create(self, request, pk=None):
        task = self.get_object()

        if not ProjectMember.objects.filter(project=task.project, user=request.user).exists():
            return Response(
                {
                    'error': 'Вы не участник проекта. Увы.'
                },
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = TaskCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, task=task)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['get'], permission_classes=[IsAuthenticated])
    def comments_list(self, request, pk=None):
        task = self.get_object()

        if not ProjectMember.objects.filter(project=task.project, user=request.user).exists():
            return Response(
                {
                    'error': 'Вы не участник проекта. Увы.'
                },
                status=status.HTTP_403_FORBIDDEN
            )

        comments = task.comments.all()
        serializer = TaskCommentSerializer(comments, many=True)
        return Response(serializer.data)

