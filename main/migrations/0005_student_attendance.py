# Generated by Django 3.1 on 2020-09-08 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_student_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='attendance',
            field=models.IntegerField(default=0),
        ),
    ]
