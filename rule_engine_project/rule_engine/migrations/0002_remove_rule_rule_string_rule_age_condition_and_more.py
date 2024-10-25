# Generated by Django 5.1.2 on 2024-10-25 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule_engine', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rule',
            name='rule_string',
        ),
        migrations.AddField(
            model_name='rule',
            name='age_condition',
            field=models.CharField(default='>=0', max_length=255),
        ),
        migrations.AddField(
            model_name='rule',
            name='department_condition',
            field=models.CharField(default='Any', max_length=255),
        ),
        migrations.AddField(
            model_name='rule',
            name='experience_condition',
            field=models.CharField(default='>=0', max_length=255),
        ),
        migrations.AddField(
            model_name='rule',
            name='salary_condition',
            field=models.CharField(default='>=0', max_length=255),
        ),
        migrations.DeleteModel(
            name='Node',
        ),
    ]