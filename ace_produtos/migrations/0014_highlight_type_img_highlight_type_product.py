# Generated by Django 4.2.5 on 2023-10-11 18:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ace_produtos", "0013_highlight"),
    ]

    operations = [
        migrations.AddField(
            model_name="highlight",
            name="type_img",
            field=models.CharField(
                choices=[
                    ("big", "Destaque Principal - Slider"),
                    ("medium", "Destaque Home"),
                    ("small", "Destaque Menu"),
                ],
                default="default",
                max_length=100,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="highlight",
            name="type_product",
            field=models.CharField(
                choices=[
                    ("t-shirt", "Camiseta"),
                    ("shirt", "Camisa"),
                    ("pants", "Calça"),
                    ("shorts", "Shorts"),
                    ("jacket", "Jaqueta"),
                    ("sweater", "Suéter"),
                    ("sweatpants", "Calça de Moletom"),
                    ("hoodie", "Moletom"),
                    ("sneaker", "Tênis"),
                ],
                default="default",
                max_length=100,
            ),
            preserve_default=False,
        ),
    ]
