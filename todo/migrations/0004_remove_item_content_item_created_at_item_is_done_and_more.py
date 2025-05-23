# Generated by Django 4.1.2 on 2024-11-19 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0003_rename_description_item_content_remove_item_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="item",
            name="content",
        ),
        migrations.AddField(
            model_name="item",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="item",
            name="is_done",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="item",
            name="title",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
