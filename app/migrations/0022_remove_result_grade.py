# Generated by Django 5.0.3 on 2024-06-21 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_result_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='result',
            name='grade',
        ),
    ]