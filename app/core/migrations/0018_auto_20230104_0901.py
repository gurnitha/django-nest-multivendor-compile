# Generated by Django 3.2 on 2023-01-04 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20230104_0859'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='addr_address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='addr_status',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='addr_user',
            new_name='user',
        ),
    ]