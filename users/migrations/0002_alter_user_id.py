# Generated by Django 5.0.6 on 2024-06-10 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.IntegerField(
                default=2,
                editable=False,
                primary_key=True,
                serialize=False,
                verbose_name="id_клиента",
            ),
        ),
    ]
