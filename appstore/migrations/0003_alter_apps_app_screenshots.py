# Generated by Django 5.0.3 on 2024-03-15 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0002_apps_app_screenshots_alter_apps_app_package_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apps',
            name='app_screenshots',
            field=models.JSONField(default=list, verbose_name='Images'),
        ),
    ]
