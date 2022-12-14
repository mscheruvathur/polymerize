# Generated by Django 4.1.3 on 2022-11-19 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_admin_password_administrator_password_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('added_by', models.CharField(default='Anonymous', max_length=255, null=True)),
                ('access_token', models.TextField()),
                ('refresh_token', models.TextField()),
                ('ip_address', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('is_revoked', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('added_by', models.CharField(default='Anonymous', max_length=255, null=True)),
                ('employeename', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('phone', models.CharField(blank=True, max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('is_verified', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(blank=True, null=True)),
                ('company', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('added_by', models.CharField(default='Anonymous', max_length=255, null=True)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=255, unique=True)),
                ('title', models.CharField(blank=True, default='', max_length=255)),
                ('keywords', models.TextField(blank=True, default='', max_length=255)),
                ('description', models.TextField(blank=True, default='', max_length=255)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='company',
        ),
        migrations.RemoveField(
            model_name='usertoken',
            name='user',
        ),
        migrations.RenameField(
            model_name='admin',
            old_name='username',
            new_name='adminname',
        ),
        migrations.RemoveField(
            model_name='authcode',
            name='administrator',
        ),
        migrations.RemoveField(
            model_name='authcode',
            name='user',
        ),
        migrations.AlterField(
            model_name='admin',
            name='company',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
        migrations.DeleteModel(
            name='Administrator',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='UserToken',
        ),
        migrations.AddField(
            model_name='authtoken',
            name='employee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.employee'),
        ),
        migrations.AddField(
            model_name='authcode',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.employee'),
        ),
    ]
