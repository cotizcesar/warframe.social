# Generated by Django 2.1 on 2018-09-06 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0019_auto_20180906_1656'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weapon',
            options={},
        ),
        migrations.AlterField(
            model_name='weapon',
            name='slug',
            field=models.SlugField(),
        ),
    ]
