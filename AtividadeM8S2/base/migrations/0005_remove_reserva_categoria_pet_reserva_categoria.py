# Generated by Django 4.2.5 on 2023-12-21 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_reserva_categoria_pet"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="reserva",
            name="categoria_pet",
        ),
        migrations.AddField(
            model_name="reserva",
            name="categoria",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base.categoria",
            ),
        ),
    ]
