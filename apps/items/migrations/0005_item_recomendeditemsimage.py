# Generated by Django 3.2.7 on 2022-02-22 10:46

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0004_remove_item_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='recomendeditemsimage',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='recomendeditem'),
        ),
    ]
