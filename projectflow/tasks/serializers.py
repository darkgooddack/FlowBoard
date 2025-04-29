from rest_framework import serializers

from django.contrib.auth import get_user_model

from projects.models import Project

User = get_user_model()

from .models import Status, Label, Task, TaskComment


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    assignees = serializers.SlugRelatedField(
        many=True,
        slug_field='username',
        queryset=User.objects.all()
    )
    labels = serializers.SlugRelatedField(
        many=True,
        slug_field='name',
        queryset=Label.objects.all()
    )
    status = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Status.objects.all()
    )
    project = serializers.SlugRelatedField(
        slug_field='name',
        queryset=Project.objects.all()
    )
    created_by = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('created_by',)


class TaskCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    task = serializers.StringRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = TaskComment
        fields = '__all__'
        read_only_fields = ('user', 'task', 'created_at')