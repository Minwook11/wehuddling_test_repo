# Generated by Django 3.1.3 on 2020-11-27 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='provider',
            new_name='provider_id',
        ),
    ]
