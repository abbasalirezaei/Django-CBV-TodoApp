# Generated by Django 4.2.4 on 2023-08-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
