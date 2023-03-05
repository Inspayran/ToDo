from datetime import datetime

from rest_framework import serializers
from .models import Task
from rest_framework.serializers import HyperlinkedIdentityField


class TaskSerializer(serializers.ModelSerializer):
    url = HyperlinkedIdentityField(view_name='api_detail_update', lookup_field='pk')

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'url']


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description']

    def create(self, validated_data):
        task = Task.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
        )
        return task


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        # fields = ['title', 'description', 'completed']
        # exclude = ('completed_at',)
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)
        if instance.completed:
            instance.completed_at = datetime.now()
        else:
            instance.completed_at = None
        instance.save()
        return instance

