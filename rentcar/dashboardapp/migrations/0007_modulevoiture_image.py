# Generated by Django 5.0.3 on 2024-04-10 14:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dashboardapp", "0006_voiture_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="modulevoiture",
            name="image",
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]