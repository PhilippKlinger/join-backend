# Generated by Django 5.0.3 on 2024-03-24 12:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0003_contact_alter_task_assigned_to'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(related_name='assigned_tasks', to=settings.AUTH_USER_MODEL),
        ),
    ]
