# Generated by Django 5.0.6 on 2024-06-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnimeApp', '0002_anime_character_id_character_character_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='season_year',
            field=models.IntegerField(default=2024),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='anime',
            name='season',
            field=models.CharField(choices=[('WINTER', 'Winter'), ('SPRING', 'Spring'), ('SUMMER', 'Summer'), ('FALL', 'Fall')], max_length=10),
        ),
    ]
