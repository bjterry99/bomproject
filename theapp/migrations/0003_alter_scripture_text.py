# Generated by Django 3.2.8 on 2022-02-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0002_scripture_tip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scripture',
            name='text',
            field=models.CharField(default='text', max_length=2000, verbose_name='Words'),
        ),
    ]