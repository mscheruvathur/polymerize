# Generated by Django 4.1.3 on 2022-11-20 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_authcode_aministrator'),
    ]

    operations = [
        migrations.RenameField(
            model_name='authcode',
            old_name='aministrator',
            new_name='administrator',
        ),
    ]
