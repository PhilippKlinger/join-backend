# Generated by Django 5.0.3 on 2024-04-05 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('join', '0018_category_color'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='status',
            new_name='stat',
        ),
        migrations.AlterField(
            model_name='category',
            name='color',
            field=models.CharField(default='red', max_length=15),
        ),
    ]
