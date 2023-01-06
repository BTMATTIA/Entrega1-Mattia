# Generated by Django 4.1.4 on 2022-12-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppEI', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('valoracion', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Comedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('valoracion', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Terror',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('valoracion', models.IntegerField(max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Equipo',
        ),
        migrations.DeleteModel(
            name='Estadio',
        ),
        migrations.DeleteModel(
            name='Jugador',
        ),
        migrations.DeleteModel(
            name='Liga',
        ),
    ]