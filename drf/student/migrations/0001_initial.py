# Generated by Django 3.2.12 on 2022-04-15 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_reg_number', models.TextField(unique=True)),
                ('student_name', models.TextField()),
                ('student_email', models.TextField()),
                ('student_mobile', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
