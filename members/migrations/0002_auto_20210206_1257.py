# Generated by Django 3.1.6 on 2021-02-06 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membersrobo',
            name='photo',
            field=models.ImageField(blank=True, default='profile_pics/default.png', null=True, upload_to='profile_pics'),
        ),
    ]
