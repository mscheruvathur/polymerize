# Generated by Django 4.1.3 on 2022-11-19 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_authcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='password',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='administrator',
            name='password',
            field=models.CharField(default=0.0, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
