# Generated by Django 4.2.5 on 2023-10-05 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ace_produtos", "0002_produto_imagem"),
    ]

    operations = [
        migrations.AddField(
            model_name="produto",
            name="cores",
            field=models.CharField(default="default", max_length=255),
            preserve_default=False,
        ),
    ]
