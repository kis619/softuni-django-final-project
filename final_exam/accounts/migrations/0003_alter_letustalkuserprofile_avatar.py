# Generated by Django 5.0.3 on 2024-04-06 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_userprofile_letustalkuserprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letustalkuserprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]
