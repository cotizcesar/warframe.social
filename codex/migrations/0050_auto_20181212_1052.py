# Generated by Django 2.1.4 on 2018-12-12 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codex', '0049_warframe_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warframe',
            name='release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
