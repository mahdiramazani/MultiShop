# Generated by Django 4.1 on 2022-08-31 14:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Acount_app', '0032_user_first_name_user_image_user_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otc',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 31, 14, 15, 46, 795303, tzinfo=datetime.timezone.utc)),
        ),
    ]
