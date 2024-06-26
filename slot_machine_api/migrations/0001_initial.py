# Generated by Django 5.0.6 on 2024-06-24 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SlotMatrix',
            fields=[
                ('slot_id', models.AutoField(primary_key=True, serialize=False)),
                ('matrix', models.JSONField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'slot_matrices',
            },
        ),
    ]
