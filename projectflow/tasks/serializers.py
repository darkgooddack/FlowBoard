from rest_framework import serializers

from django.contrib.auth import get_user_model

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
    assignees = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)
    labels = serializers.PrimaryKeyRelatedField(many=True, queryset=Label.objects.all(), required=False)
    status = serializers.PrimaryKeyRelatedField(queryset=Status.objects.all())

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('created_by', )

class TaskCommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = TaskComment
        fields = '__all__'
        read_only_fields = ('user',)