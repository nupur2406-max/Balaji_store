# Generated by Django 3.1 on 2020-08-26 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=60)),
                ('product_price', models.IntegerField()),
                ('product_description', models.CharField(max_length=1000)),
                ('product_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
