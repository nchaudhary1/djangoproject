# Generated by Django 3.2 on 2022-10-15 09:36

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
                ('name', models.CharField(max_length=255)),
                ('course', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
