# Generated by Django 4.2.2 on 2023-11-09 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eFile', '0006_alter_issueletter_lettertext'),
    ]

    operations = [
        migrations.AddField(
            model_name='issueletter',
            name='LetterDate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
