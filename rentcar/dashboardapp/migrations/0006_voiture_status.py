# Generated by Django 5.0.3 on 2024-04-10 02:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboardapp", "0005_remove_voiture_type_modulevoiture_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="voiture",
            name="status",
            field=models.CharField(max_length=255, null=True),
        ),
    ]