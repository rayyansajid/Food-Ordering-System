# Generated by Django 4.2.2 on 2023-12-30 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delicrave', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='catalogitem',
        ),
        migrations.AddField(
            model_name='cart',
            name='catalogitem',
            field=models.OneToOneField(blank=True, db_column='CatalogItem', null=True, on_delete=django.db.models.deletion.CASCADE, to='delicrave.catalogitem'),
        ),
    ]
