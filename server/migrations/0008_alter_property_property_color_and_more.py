# Generated by Django 4.1.7 on 2023-03-12 16:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0007_alter_property_property_formula"),
    ]

    operations = [
        migrations.AlterField(
            model_name="property",
            name="property_color",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Цвет свойства"
            ),
        ),
        migrations.AlterField(
            model_name="property",
            name="property_desc",
            field=models.CharField(
                blank=True, max_length=1000, null=True, verbose_name="Описание свойства"
            ),
        ),
    ]
