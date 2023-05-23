from rest_framework import serializers
from .models import TaskTracker

class TaskTrackerSerializer(serializers.ModelSerializer):

    class Meta: # default özelliklerin belirlendiği yer
        model = TaskTracker
        fields = "__all__"
        # exclude = []