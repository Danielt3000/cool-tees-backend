# Generated by Django 3.2.7 on 2022-02-23 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recomendeditems', '0002_rename_image_recomendeditem_recomendedimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recomendeditem',
            old_name='name',
            new_name='recomendedname',
        ),
        migrations.RenameField(
            model_name='recomendeditem',
            old_name='price',
            new_name='recomendedprice',
        ),
    ]
