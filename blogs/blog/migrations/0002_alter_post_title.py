# Generated by Django 4.0.4 on 2022-05-15 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30, verbose_name='Заголовок'),
        ),
    ]
