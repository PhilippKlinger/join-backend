# Generated by Django 5.0.3 on 2024-03-25 15:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0011_task_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subtask',
            name='task',
        ),
        migrations.CreateModel(
            name='TaskSubTask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subtask', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='join.subtask')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='join.task')),
            ],
        ),
    ]
