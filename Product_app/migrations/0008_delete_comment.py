# Generated by Django 4.1 on 2022-08-31 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Product_app', '0007_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
