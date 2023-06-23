# Generated by Django 4.1.7 on 2023-06-13 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RustezeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('prod_id', models.IntegerField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
                ('precio', models.IntegerField(max_length=20)),
            ],
            options={
                'ordering': ['prod_id'],
            },
        ),
    ]
