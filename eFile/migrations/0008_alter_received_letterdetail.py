# Generated by Django 4.2.2 on 2023-11-09 15:44

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eFile', '0007_issueletter_letterdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='received',
            name='LetterDetail',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]