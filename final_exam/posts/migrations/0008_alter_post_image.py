# Generated by Django 5.0.3 on 2024-04-09 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='posts/default-post-image.jpg', null=True, upload_to='posts/'),
        ),
    ]
