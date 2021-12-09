# Generated by Django 4.0 on 2021-12-08 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myplants_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=200)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myplants_app.plant')),
            ],
        ),
    ]