# Generated by Django 2.2.1 on 2019-08-03 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_auto_20190802_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
