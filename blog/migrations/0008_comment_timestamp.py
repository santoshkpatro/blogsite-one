# Generated by Django 3.0.7 on 2020-06-14 03:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200511_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
