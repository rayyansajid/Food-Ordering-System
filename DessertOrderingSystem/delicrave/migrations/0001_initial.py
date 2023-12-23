# Generated by Django 4.2.4 on 2023-12-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
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
                ('username', models.CharField(db_column='UserName', max_length=11)),
                ('password', models.CharField(db_column='Password', max_length=10)),
                ('name', models.CharField(db_column='Name', max_length=20)),
                ('contact', models.CharField(db_column='contact', max_length=11, unique=1)),
                ('email', models.EmailField(db_column='Email', max_length=254)),
                ('address', models.CharField(db_column='Address', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Desert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='Name', max_length=10)),
                ('stockquantity', models.IntegerField(blank=True, db_column='Stock Quantity', null=True)),
                ('description', models.CharField(db_column='Description', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(blank=True, db_column='Rating', null=True)),
                ('review', models.CharField(db_column='Review', max_length=100, null=True)),
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
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitname', models.CharField(db_column='Name', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.ManyToManyField(db_column='Customer', to='delicrave.customer')),
                ('Desert', models.ManyToManyField(db_column='Desert', to='delicrave.desert')),
            ],
        ),
        migrations.CreateModel(
            name='FlavorCat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category', models.ManyToManyField(db_column='Category', to='delicrave.category')),
                ('Flavor', models.ManyToManyField(db_column='Flavor', to='delicrave.flavor')),
            ],
        ),
        migrations.CreateModel(
            name='Catalog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Price', models.FloatField(blank=True, default=0.0, null=True)),
                ('Desert', models.ManyToManyField(db_column='Desert', to='delicrave.desert')),
                ('Unit', models.ManyToManyField(db_column='Unit', to='delicrave.unit')),
            ],
        ),
    ]
