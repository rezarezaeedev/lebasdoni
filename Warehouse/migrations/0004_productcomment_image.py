# Generated by Django 4.2.3 on 2023-08-10 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Warehouse', '0003_alter_productinfo_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcomment',
            name='image',
            field=models.ImageField(default='exit', upload_to='Media/uploded/'),
            preserve_default=False,
        ),
    ]