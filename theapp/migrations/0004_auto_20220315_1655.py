# Generated by Django 3.2.8 on 2022-03-15 22:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theapp', '0003_alter_scripture_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='admin', max_length=20, verbose_name='Username')),
                ('password', models.CharField(default='1234', max_length=50, verbose_name='Password')),
            ],
            options={
                'db_table': 'user',
            },
        ),
        migrations.RemoveField(
            model_name='scripture',
            name='favorite',
        ),
        migrations.CreateModel(
            name='favorite',
            fields=[
                ('fav_id', models.AutoField(primary_key=True, serialize=False)),
                ('scriptureid', models.ForeignKey(default='default', on_delete=django.db.models.deletion.DO_NOTHING, to='theapp.scripture', verbose_name='Scripture')),
                ('userid', models.ForeignKey(default='default', on_delete=django.db.models.deletion.DO_NOTHING, to='theapp.user', verbose_name='User')),
            ],
            options={
                'db_table': 'favorite',
            },
        ),
    ]
