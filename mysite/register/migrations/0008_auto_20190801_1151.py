# Generated by Django 2.2.3 on 2019-08-01 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20190801_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='top_image',
            field=models.ImageField(blank=True, upload_to='media/', verbose_name='トップ画像'),
        ),
    ]
