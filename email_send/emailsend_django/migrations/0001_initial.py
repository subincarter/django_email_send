# Generated by Django 3.0.2 on 2020-01-23 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emailSend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('body', models.CharField(max_length=20)),
                ('image', models.FileField(upload_to='image/')),
            ],
        ),
    ]