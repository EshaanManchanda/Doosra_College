# Generated by Django 4.0.5 on 2022-06-29 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('phone_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('prof_desc', models.CharField(max_length=50)),
            ],
        ),
    ]
