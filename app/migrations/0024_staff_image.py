# Generated by Django 5.0.3 on 2024-06-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_staff_feedback_status_student_feedback_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(default=2, upload_to='media/img'),
            preserve_default=False,
        ),
    ]
