# Generated by Django 4.1.7 on 2023-03-20 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SocialTravel', '0002_post_publisher'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts'),
        ),
    ]
