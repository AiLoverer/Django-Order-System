# Generated by Django 5.2.3 on 2025-06-24 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('nickname', models.CharField(max_length=50)),
                ('password_hash', models.CharField(max_length=100)),
                ('password_salt', models.CharField(max_length=50)),
                ('status', models.IntegerField(default=1)),
                ('create_at', models.DateTimeField(default=datetime.datetime.now)),
                ('update_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
