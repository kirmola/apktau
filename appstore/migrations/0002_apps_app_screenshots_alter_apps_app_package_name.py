# Generated by Django 5.0.3 on 2024-03-15 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apps',
            name='app_screenshots',
            field=models.JSONField(default=dict, verbose_name='Images'),
        ),
        migrations.AlterField(
            model_name='apps',
            name='app_package_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Package Name'),
        ),
    ]
