# Generated by Django 2.2.3 on 2019-08-01 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_auto_20190801_0140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='file',
        ),
        migrations.AlterField(
            model_name='user',
            name='top_image',
            field=models.ImageField(upload_to='media/', verbose_name='トップ画像'),
        ),
    ]
