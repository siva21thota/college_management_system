# Generated by Django 5.0.3 on 2024-05-31 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_staff_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_notification',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]