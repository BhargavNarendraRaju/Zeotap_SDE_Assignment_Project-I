# Generated by Django 5.1.2 on 2024-10-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rule_engine', '0006_rename_sql_query_rule_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='query',
            field=models.CharField(max_length=255),
        ),
    ]
