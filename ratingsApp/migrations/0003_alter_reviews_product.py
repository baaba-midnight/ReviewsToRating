# Generated by Django 5.0.7 on 2024-07-24 09:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratingsApp', '0002_reviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ratingsApp.product'),
        ),
    ]
