# Generated by Django 4.2.7 on 2023-11-29 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fs", "0002_matter_mattertype_sender_received_matter_mattertype"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sender",
            name="Pincode",
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name="sender",
            name="SenderOfficeH",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="sender",
            name="SenderPlaceH",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="sender",
            name="SenderPostH",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="sender",
            name="SenderShortNameH",
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]