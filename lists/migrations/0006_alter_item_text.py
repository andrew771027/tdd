# Generated by Django 4.1.5 on 2023-05-08 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_alter_item_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.TextField(default=''),
        ),
    ]