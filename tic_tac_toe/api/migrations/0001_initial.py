# Generated by Django 3.1.3 on 2020-11-08 17:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("game_id", models.UUIDField(default=uuid.uuid4, editable=False)),
                ("board", models.TextField(default="012345678", max_length=9)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("RUNNING", " The game is running!"),
                            ("X_WON", " Player X won the game!"),
                            ("O_WON", "Player O won the game!"),
                            ("DRAW", "The game is not active."),
                        ],
                        max_length=7,
                    ),
                ),
            ],
        ),
    ]