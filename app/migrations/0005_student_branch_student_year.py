# Generated by Django 5.0.3 on 2024-04-23 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_student_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='Branch',
            field=models.CharField(default='CSE', max_length=50),
        ),
        migrations.AddField(
            model_name='student',
            name='year',
            field=models.CharField(default='2021', max_length=50),
        ),
    ]
