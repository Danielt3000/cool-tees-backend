# Generated by Django 2.2.6 on 2022-02-28 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('favourite_items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favouriteitem',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]