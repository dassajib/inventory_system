# Generated by Django 3.2.12 on 2023-04-15 20:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_template', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredienttemplate',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='product_template.producttemplate'),
            preserve_default=False,
        ),
    ]
