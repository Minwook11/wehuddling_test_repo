# Generated by Django 3.1.3 on 2020-11-29 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_remove_customer_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='', max_length=256),
        ),
    ]
