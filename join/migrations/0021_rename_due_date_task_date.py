# Generated by Django 5.0.3 on 2024-04-05 08:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0020_alter_task_stat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='due_date',
            new_name='date',
        ),
    ]