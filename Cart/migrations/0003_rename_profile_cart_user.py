# Generated by Django 4.2.3 on 2023-08-08 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0002_alter_cart_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='profile',
            new_name='user',
        ),
    ]