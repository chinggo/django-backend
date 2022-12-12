# Generated by Django 4.0.8 on 2022-10-27 07:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0007_alter_contestlikes_contest_alter_contestlikes_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contestlikes",
            name="contest",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contest_likes",
                to="core.contest",
            ),
        ),
        migrations.AlterField(
            model_name="contestlikes",
            name="user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="post_likes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
