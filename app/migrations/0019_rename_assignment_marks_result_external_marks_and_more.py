# Generated by Django 5.0.3 on 2024-06-21 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='assignment_marks',
            new_name='external_marks',
        ),
        migrations.RenameField(
            model_name='result',
            old_name='exam_marks',
            new_name='internal_marks',
        ),
    ]
