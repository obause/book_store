# Generated by Django 4.1.3 on 2022-12-10 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0002_book_is_bestselling_alter_book_price_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="slug",
            field=models.SlugField(default=""),
        ),
    ]