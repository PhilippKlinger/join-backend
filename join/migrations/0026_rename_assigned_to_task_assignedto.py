# Generated by Django 5.0.3 on 2024-04-05 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0025_task_subtasks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='assigned_to',
            new_name='assignedTo',
        ),
    ]
