# Generated by Django 4.2.7 on 2023-11-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Branch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("BranchName", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="FileInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("FileSl", models.IntegerField(default=0)),
                (
                    "FileType",
                    models.CharField(
                        choices=[
                            ("Corr", "Correspondence"),
                            ("Saction", "Sanction"),
                            ("L-Case", "Legal Case"),
                            ("CashConveyance", "Cash Conveyance"),
                            ("Duplicate", "Duplicate"),
                            ("DeceasedClaim", "Deceased Claim"),
                            ("CourtCase", "Court Case"),
                            ("Statement", "Statement"),
                        ],
                        max_length=15,
                    ),
                ),
                ("FileName", models.CharField(max_length=255)),
                ("FileNo", models.CharField(blank=True, max_length=50, null=True)),
                (
                    "ActiveStatus",
                    models.CharField(
                        choices=[("Active", "Active"), ("Closed", "Closed")],
                        default="Active",
                        max_length=10,
                    ),
                ),
                ("OpenDate", models.DateField()),
                ("CloseDate", models.DateField(blank=True, null=True)),
                ("RelatedOffice", models.CharField(max_length=100)),
                ("FileLocation", models.CharField(max_length=10)),
                (
                    "WordFile",
                    models.FileField(blank=True, null=True, upload_to="word_files/"),
                ),
            ],
        ),
    ]
