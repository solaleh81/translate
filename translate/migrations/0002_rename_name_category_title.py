# Generated by Django 5.0.1 on 2024-01-12 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translate', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='title',
        ),
    ]
