# Generated by Django 5.0.5 on 2024-05-07 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filmovi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naslov', models.CharField(max_length=120)),
                ('sadrzaj', models.CharField(max_length=520)),
            ],
        ),
    ]
