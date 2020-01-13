# Generated by Django 3.0 on 2019-12-27 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chambre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=50)),
                ('lieu', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('altiude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Chambre')),
            ],
        ),
        migrations.AddField(
            model_name='chambre',
            name='cite',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Cite'),
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.CharField(max_length=50)),
                ('moderne', models.BooleanField(default=False)),
                ('equipement', models.BooleanField(default=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('chambre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.Chambre')),
            ],
        ),
    ]