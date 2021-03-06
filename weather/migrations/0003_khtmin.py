# Generated by Django 2.2 on 2019-04-15 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20190415_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='KhTmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('year', models.PositiveIntegerField()),
                ('month', models.PositiveIntegerField()),
                ('country', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Min Temperature',
                'db_table': 'kh_tmin',
                'unique_together': {('year', 'month', 'country')},
            },
        ),
    ]
