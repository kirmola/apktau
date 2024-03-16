# Generated by Django 5.0.3 on 2024-03-16 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appstore', '0005_alter_apps_package_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apps',
            name='app_screenshots',
        ),
        migrations.AddField(
            model_name='apps',
            name='screenshot_1',
            field=models.ImageField(default=None, upload_to=None, verbose_name='Screenshot_1'),
        ),
        migrations.AddField(
            model_name='apps',
            name='screenshot_2',
            field=models.ImageField(default=None, upload_to=None, verbose_name='Screenshot_2'),
        ),
        migrations.AddField(
            model_name='apps',
            name='screenshot_3',
            field=models.ImageField(default=None, upload_to=None, verbose_name='Screenshot_3'),
        ),
        migrations.AddField(
            model_name='apps',
            name='screenshot_4',
            field=models.ImageField(default=None, upload_to=None, verbose_name='Screenshot_4'),
        ),
        migrations.AddField(
            model_name='apps',
            name='screenshot_5',
            field=models.ImageField(default=None, upload_to=None, verbose_name='Screenshot_5'),
        ),
        migrations.AddField(
            model_name='apps',
            name='screenshot_6',
            field=models.ImageField(default=None, upload_to=None, verbose_name='Screenshot_6'),
        ),
        migrations.AddField(
            model_name='apps',
            name='screenshot_7',
            field=models.ImageField(default=None, upload_to=None, verbose_name='Screenshot_7'),
        ),
        migrations.AddField(
            model_name='apps',
            name='screenshot_8',
            field=models.ImageField(default=None, upload_to=None, verbose_name='Screenshot_8'),
        ),
    ]