# Generated by Django 4.2.13 on 2024-06-22 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Books', '0002_bookreviewmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreviewmodel',
            name='reviewer',
            field=models.CharField(default='a', max_length=100),
            preserve_default=False,
        ),
    ]
