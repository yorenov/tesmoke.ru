# Generated by Django 5.0.2 on 2024-05-11 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_referral_statsdata'),
    ]

    operations = [
        migrations.RenameField(
            model_name='referrallink',
            old_name='text',
            new_name='referal',
        ),
    ]
