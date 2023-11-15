# Generated by Django 4.2.5 on 2023-11-13 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ace_produtos", "0020_product_new_product_offer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="type_accessory",
        ),
        migrations.AlterField(
            model_name="product",
            name="type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="produtos",
                to="ace_produtos.typeaccessory",
            ),
        ),
    ]
