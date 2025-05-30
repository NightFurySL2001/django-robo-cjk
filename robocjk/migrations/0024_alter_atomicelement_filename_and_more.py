# Generated by Django 5.0.1 on 2025-04-25 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("robocjk", "0023_alter_atomicelement_status_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="atomicelement",
            name="filename",
            field=models.CharField(
                blank=True,
                help_text="(.glif xml output filename, autodetected from xml data)",
                max_length=100,
                verbose_name="Filename",
            ),
        ),
        migrations.AlterField(
            model_name="atomicelement",
            name="name",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text="(autodetected from xml data)",
                max_length=100,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="atomicelementlayer",
            name="filename",
            field=models.CharField(
                blank=True,
                help_text="(.glif xml output filename, autodetected from xml data)",
                max_length=100,
                verbose_name="Filename",
            ),
        ),
        migrations.AlterField(
            model_name="atomicelementlayer",
            name="name",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text="(autodetected from xml data)",
                max_length=100,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="characterglyph",
            name="filename",
            field=models.CharField(
                blank=True,
                help_text="(.glif xml output filename, autodetected from xml data)",
                max_length=100,
                verbose_name="Filename",
            ),
        ),
        migrations.AlterField(
            model_name="characterglyph",
            name="name",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text="(autodetected from xml data)",
                max_length=100,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="characterglyphlayer",
            name="filename",
            field=models.CharField(
                blank=True,
                help_text="(.glif xml output filename, autodetected from xml data)",
                max_length=100,
                verbose_name="Filename",
            ),
        ),
        migrations.AlterField(
            model_name="characterglyphlayer",
            name="name",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text="(autodetected from xml data)",
                max_length=100,
                verbose_name="Name",
            ),
        ),
        migrations.AlterField(
            model_name="deepcomponent",
            name="filename",
            field=models.CharField(
                blank=True,
                help_text="(.glif xml output filename, autodetected from xml data)",
                max_length=100,
                verbose_name="Filename",
            ),
        ),
        migrations.AlterField(
            model_name="deepcomponent",
            name="name",
            field=models.CharField(
                blank=True,
                db_index=True,
                help_text="(autodetected from xml data)",
                max_length=100,
                verbose_name="Name",
            ),
        ),
    ]
