# Generated by Django 4.1.3 on 2022-11-10 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0008_review"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="name",
            new_name="customer",
        ),
    ]