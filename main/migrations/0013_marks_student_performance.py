# Generated by Django 3.1 on 2020-09-18 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_marks_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='student_performance',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
