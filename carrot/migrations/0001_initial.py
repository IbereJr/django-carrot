# Generated by Django 2.0.5 on 2018-05-08 12:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies: list = [
    ]

    operations = [
        migrations.CreateModel(
            name='MessageLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PUBLISHED', 'Published'), ('IN_PROGRESS', 'In progress'), ('FAILED', 'Failed'), ('COMPLETED', 'Completed')], default='PUBLISHED', max_length=11)),
                ('exchange', models.CharField(blank=True, max_length=200, null=True)),
                ('queue', models.CharField(blank=True, max_length=200, null=True)),
                ('routing_key', models.CharField(blank=True, max_length=200, null=True)),
                ('uuid', models.CharField(max_length=200)),
                ('priority', models.PositiveIntegerField(default=0)),
                ('task', models.CharField(max_length=200)),
                ('task_args', models.TextField(blank=True, null=True, verbose_name='Task positional arguments')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Task keyword arguments')),
                ('exception', models.TextField(blank=True, null=True)),
                ('traceback', models.TextField(blank=True, null=True)),
                ('output', models.TextField(blank=True, null=True)),
                ('publish_time', models.DateTimeField(blank=True, null=True)),
                ('failure_time', models.DateTimeField(blank=True, null=True)),
                ('completion_time', models.DateTimeField(blank=True, null=True)),
                ('log', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ('-failure_time', '-completion_time', 'status', '-priority', '-publish_time'),
            },
        ),
        migrations.CreateModel(
            name='ScheduledTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interval_type', models.CharField(choices=[('seconds', 'seconds'), ('minutes', 'minutes'), ('hours', 'hours'), ('days', 'days')], default='seconds', max_length=200)),
                ('interval_count', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)])),
                ('exchange', models.CharField(blank=True, max_length=200, null=True)),
                ('routing_key', models.CharField(blank=True, max_length=200, null=True)),
                ('queue', models.CharField(blank=True, max_length=200, null=True)),
                ('task', models.CharField(max_length=200)),
                ('task_args', models.TextField(blank=True, null=True, verbose_name='Positional arguments')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Keyword arguments')),
                ('active', models.BooleanField(default=True)),
                ('next_time', models.DateTimeField(null=True, blank=True)),
                ('start_time', models.PositiveIntegerField(default=0)),
                ('priority', models.PositiveIntegerField(default=0))
            ],
        ),
    ]
