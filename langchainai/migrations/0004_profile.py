# Generated by Django 5.1.6 on 2025-02-24 18:54

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('langchainai', '0003_rename_configuration_keyconfiguration'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namespace', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('openai_api_key', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('pinecone_api_key', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('metadata', models.JSONField(blank=True, default=dict, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
