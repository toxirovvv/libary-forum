# Generated by Django 5.0.4 on 2024-06-04 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_post_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='book name', max_length=150, verbose_name='post_name'),
        ),
    ]
