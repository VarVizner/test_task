# Generated by Django 3.2.13 on 2024-06-09 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Elements',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('code', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=5, max_digits=19)),
            ],
        ),
    ]
