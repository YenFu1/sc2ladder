# Generated by Django 3.0.4 on 2020-03-20 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_ladder"),
    ]

    operations = [
        migrations.AddField(
            model_name="player",
            name="game_link",
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
