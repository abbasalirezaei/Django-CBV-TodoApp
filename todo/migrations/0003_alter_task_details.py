# Generated by Django 4.2.4 on 2023-08-14 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='details',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
