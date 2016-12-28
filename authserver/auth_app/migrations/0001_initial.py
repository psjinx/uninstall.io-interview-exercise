# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 05:46
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated at')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
            ],
            options={
                'db_table': 'applications',
                'verbose_name': 'application',
                'verbose_name_plural': 'applications',
            },
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated at')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auth_app.Organization')),
            ],
            options={
                'db_table': 'organizations',
                'verbose_name': 'organization',
                'verbose_name_plural': 'organizations',
            },
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated at')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='name')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
            ],
            options={
                'db_table': 'permissions',
                'verbose_name': 'permission',
                'verbose_name_plural': 'permissions',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created_at', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created at')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated at')),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.CharField(max_length=255, verbose_name='description')),
            ],
            options={
                'db_table': 'roles',
                'verbose_name': 'role',
                'verbose_name_plural': 'roles',
            },
        ),
        migrations.CreateModel(
            name='RolePermissionAssociation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('permission', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.Permission')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.Role')),
            ],
            options={
                'db_table': 'roles_permissions',
                'verbose_name': 'role + permission association',
                'verbose_name_plural': 'role + permission associations',
            },
        ),
        migrations.CreateModel(
            name='RoleUserOrgAssociation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.Organization')),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.Role')),
            ],
            options={
                'db_table': 'roles_users_org',
                'verbose_name': 'role + user + organization association',
                'verbose_name_plural': 'role + user + organization associations',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('date_joined', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='date joined')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('updated_at', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='updated at')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
            ],
            options={
                'db_table': 'users',
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='roleuserorgassociation',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_app.User'),
        ),
        migrations.AlterUniqueTogether(
            name='roleuserorgassociation',
            unique_together=set([('role', 'organization', 'user')]),
        ),
        migrations.AlterUniqueTogether(
            name='rolepermissionassociation',
            unique_together=set([('role', 'permission')]),
        ),
    ]