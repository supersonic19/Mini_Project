# Generated by Django 3.1 on 2020-09-07 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_course_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='main.Course'),
        ),
    ]
