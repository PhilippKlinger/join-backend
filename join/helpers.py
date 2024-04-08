from .models import SubTask
from rest_framework.response import Response
from rest_framework import status
from .serializers import SubTaskSerializer

def process_subtasks(task, subtasks_data):
    errors = []
    for subtask_data in subtasks_data:
        subtask_id = subtask_data.get('id', None)
        if subtask_id:
            subtask_instance = SubTask.objects.filter(id=subtask_id, task=task).first()
            if subtask_instance:
                subtask_serializer = SubTaskSerializer(subtask_instance, data=subtask_data, partial=True)
                if subtask_serializer.is_valid():
                    subtask_serializer.save()
                else:
                    errors.append(subtask_serializer.errors)
            else:
                errors.append({'error': 'Subtask not found or does not belong to task.'})
    return errors