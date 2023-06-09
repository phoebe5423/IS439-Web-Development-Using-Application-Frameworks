# Generated by Django 4.1 on 2023-05-04 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("fandom", "0006_activity_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activity",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="activity",
                to="fandom.role",
            ),
        ),
    ]
