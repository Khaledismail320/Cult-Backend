# Generated by Django 4.2.4 on 2024-09-10 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.TextField()),
                ('subject', models.TextField(null=True)),
                ('inquiryType', models.TextField()),
                ('Message', models.TextField()),
            ],
        ),
    ]
