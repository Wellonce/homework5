# Generated by Django 5.0.1 on 2024-01-17 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_code_new_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='img',
            field=models.ImageField(upload_to='news/'),
        ),
        migrations.AlterField(
            model_name='new',
            name='title',
            field=models.CharField(max_length=128),
        ),
    ]