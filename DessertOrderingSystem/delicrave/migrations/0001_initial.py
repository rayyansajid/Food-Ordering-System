# Generated by Django 4.2.2 on 2023-12-30 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(db_column='UserName', max_length=10)),
                ('password', models.CharField(db_column='Password', max_length=10)),
                ('name', models.CharField(db_column='Name', max_length=20)),
                ('contact', models.CharField(db_column='contact', max_length=15, unique=1)),
                ('email', models.EmailField(db_column='Email', max_length=254)),
                ('address', models.CharField(db_column='Address', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=10)),
                ('stockquantity', models.IntegerField(blank=True, db_column='Stock Quantity', null=True)),
                ('description', models.CharField(db_column='Description', max_length=100, null=True)),
                ('category', models.ForeignKey(blank=True, db_column='Category', null=True, on_delete=django.db.models.deletion.CASCADE, to='delicrave.category')),
            ],
        ),
        migrations.CreateModel(
            name='Flavor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('status', models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], max_length=10, null=True)),
                ('totalamount', models.FloatField(blank=True, null=True)),
                ('paymethod', models.CharField(blank=True, choices=[('COD', 'COD'), ('CARD', 'CARD')], max_length=10, null=True)),
                ('rating', models.IntegerField(blank=True, db_column='Rating', null=True)),
                ('review', models.CharField(blank=True, db_column='Review', max_length=100, null=True)),
                ('customer', models.ForeignKey(db_column='customer_id', on_delete=django.db.models.deletion.CASCADE, to='delicrave.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_column='Name', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ManyToManyField(db_column='Customer', to='delicrave.customer')),
                ('dessert', models.ManyToManyField(db_column='Dessert', to='delicrave.dessert')),
            ],
        ),
        migrations.CreateModel(
            name='OrderHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('catalogitem', models.ManyToManyField(db_column='CatalogItem', to='delicrave.catalogitem')),
                ('order', models.ForeignKey(db_column='Order', on_delete=django.db.models.deletion.CASCADE, to='delicrave.order')),
            ],
        ),
        migrations.CreateModel(
            name='FlavorCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ManyToManyField(db_column='Category', to='delicrave.category')),
                ('flavor', models.ManyToManyField(db_column='Flavor', to='delicrave.flavor')),
            ],
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='dessert',
            field=models.ManyToManyField(db_column='Dessert', to='delicrave.dessert'),
        ),
        migrations.AddField(
            model_name='catalogitem',
            name='unit',
            field=models.ManyToManyField(db_column='Unit', to='delicrave.unit'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('catalogitem', models.ManyToManyField(db_column='CatalogItem', to='delicrave.catalogitem')),
                ('customer', models.ForeignKey(blank=True, db_column='Customer', null=True, on_delete=django.db.models.deletion.CASCADE, to='delicrave.customer')),
            ],
        ),
    ]
