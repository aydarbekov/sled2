# Generated by Django 2.2 on 2021-02-17 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0019_remove_product_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specification',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Спецификация'),
        ),
    ]
