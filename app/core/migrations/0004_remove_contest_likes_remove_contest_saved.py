# Generated by Django 4.0.8 on 2022-10-21 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_contest_likes_alter_contest_saved"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="contest",
            name="likes",
        ),
        migrations.RemoveField(
            model_name="contest",
            name="saved",
        ),
    ]
