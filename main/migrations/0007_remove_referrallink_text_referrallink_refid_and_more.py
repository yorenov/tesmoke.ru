# Generated by Django 5.0.6 on 2024-05-25 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_referrallink_options_alter_statsdata_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referrallink',
            name='text',
        ),
        migrations.AddField(
            model_name='referrallink',
            name='refid',
            field=models.TextField(default='ref', unique=True, verbose_name='Реферальное айди'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='referrallink',
            name='stats',
            field=models.ManyToManyField(related_name='referral_links', to='main.statsdata', verbose_name='Записи'),
        ),
        migrations.AddField(
            model_name='statsdata',
            name='city',
            field=models.CharField(blank=True, default=None, max_length=1024, null=True, verbose_name='Город'),
        ),
    ]
