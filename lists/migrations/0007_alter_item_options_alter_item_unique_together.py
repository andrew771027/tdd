# Generated by Django 4.1.5 on 2023-06-18 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0006_alter_item_text'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]