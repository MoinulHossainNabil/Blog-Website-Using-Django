# Generated by Django 2.2.1 on 2019-07-28 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20190727_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='featured',
            field=models.BooleanField(default=True),
        ),
    ]
