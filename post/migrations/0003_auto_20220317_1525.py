# Generated by Django 3.2.9 on 2022-03-17 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20220317_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='post',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
    ]
