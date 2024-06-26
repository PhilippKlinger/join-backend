# Generated by Django 5.0.3 on 2024-04-07 15:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0030_remove_task_color'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='subtasks',
        ),
        migrations.AddField(
            model_name='subtask',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='join.task'),
        ),
        migrations.AlterField(
            model_name='subtask',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
