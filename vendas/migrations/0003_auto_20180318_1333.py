# Generated by Django 2.0.1 on 2018-03-18 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0002_auto_20180311_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venda',
            name='desconto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='venda',
            name='impostos',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
