# Generated by Django 4.1.7 on 2023-03-12 11:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("server", "0003_alter_facility_cluster_id_alter_facility_dept_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facility",
            name="facility_create_date",
            field=models.DateTimeField(
                blank=True,
                default="01-01-1999",
                null=True,
                verbose_name="Дата заведения объекта",
            ),
        ),
        migrations.AlterField(
            model_name="property",
            name="unit_id",
            field=models.IntegerField(verbose_name="Идентификатор блока"),
        ),
    ]
