# Generated by Django 4.2.7 on 2023-12-02 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmarkd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dictionary',
            name='url_tag',
            field=models.CharField(default=None, max_length=2560),
        ),
    ]
