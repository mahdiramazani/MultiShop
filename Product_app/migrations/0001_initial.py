# Generated by Django 4.1 on 2022-08-30 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='product/category')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='Product_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='product/image')),
                ('price', models.CharField(max_length=50)),
                ('discount', models.CharField(blank=True, max_length=50, null=True)),
                ('score', models.IntegerField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ManyToManyField(related_name='product', to='Product_app.category')),
            ],
        ),
    ]
