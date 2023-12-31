# Generated by Django 4.2.5 on 2023-09-20 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('encuesta', '0002_clasificacion_cliente_producto_proveedor_venta_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clasificacion',
            name='cla_cod',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cli_cod',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cli_telf_1',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cli_telf_2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='prod_cod',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='prov_cod',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='prov_telf',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='venta',
            name='nro_fac',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
