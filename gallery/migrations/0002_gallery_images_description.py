# Generated by Django 3.1.6 on 2021-07-15 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery_images',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]