# Generated by Django 2.1.2 on 2018-10-10 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0004_auto_20181010_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_amount',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]
