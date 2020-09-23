# Generated by Django 2.2.3 on 2019-08-01 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_user_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='area',
            field=models.CharField(blank=True, max_length=150, verbose_name='活動領域'),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.URLField(blank=True, verbose_name='Instagramアカウント'),
        ),
        migrations.AddField(
            model_name='user',
            name='portfolio',
            field=models.CharField(blank=True, max_length=150, verbose_name='ポートフォリオ'),
        ),
        migrations.AddField(
            model_name='user',
            name='request_fee',
            field=models.CharField(blank=True, max_length=150, verbose_name='依頼料'),
        ),
        migrations.AddField(
            model_name='user',
            name='self_introduction',
            field=models.CharField(blank=True, max_length=500, verbose_name='自己PR'),
        ),
        migrations.AddField(
            model_name='user',
            name='skill',
            field=models.CharField(blank=True, max_length=150, verbose_name='技術領域'),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.URLField(blank=True, verbose_name='Twitterアカウント'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nick_name',
            field=models.CharField(max_length=30, verbose_name='ニックネーム'),
        ),
    ]
