# Generated by Django 4.2.2 on 2023-06-14 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appform', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
