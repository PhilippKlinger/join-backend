# Generated by Django 5.0.3 on 2024-03-24 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0006_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='assigned_to',
            field=models.ManyToManyField(related_name='assigned_tasks', to='join.contact'),
        ),
    ]
