# Generated by Django 5.1.1 on 2024-10-09 20:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Time_Banking", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customuser",
            options={},
        ),
        migrations.AlterModelTable(
            name="customuser",
            table="Time_Banking_CustomUser",
        ),
    ]