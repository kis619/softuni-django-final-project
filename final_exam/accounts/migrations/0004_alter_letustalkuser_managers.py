# Generated by Django 5.0.3 on 2024-04-07 09:35

import final_exam.accounts.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_letustalkuserprofile_avatar'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='letustalkuser',
            managers=[
                ('objects', final_exam.accounts.managers.LetUsTalkUserManager()),
            ],
        ),
    ]
