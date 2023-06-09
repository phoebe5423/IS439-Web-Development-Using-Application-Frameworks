# Generated by Django 4.1 on 2023-05-04 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("fandom", "0002_rename_entertainertype_style_alter_style_options_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="EntertainerGroup",
            fields=[
                (
                    "entertainer_group_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                (
                    "entertainer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="entertainer_group",
                        to="fandom.entertainer",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="entertainer_group",
                        to="fandom.group",
                    ),
                ),
            ],
            options={
                "ordering": ["entertainer", "group"],
            },
        ),
        migrations.AddConstraint(
            model_name="entertainergroup",
            constraint=models.UniqueConstraint(
                fields=("entertainer", "group"), name="unique_entertainer_group"
            ),
        ),
    ]
