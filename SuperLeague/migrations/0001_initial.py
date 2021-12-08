# Generated by Django 3.2.9 on 2021-12-04 10:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club_name', models.CharField(max_length=50)),
                ('coutry', models.CharField(max_length=3)),
                ('rating', models.IntegerField()),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goal_home', models.IntegerField(default=0)),
                ('goal_away', models.IntegerField(default=0)),
                ('away', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_game_away', to='SuperLeague.club')),
                ('home', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='club_game_hom', to='SuperLeague.club')),
            ],
        ),
    ]
