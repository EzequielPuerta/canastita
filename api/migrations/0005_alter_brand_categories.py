# Generated by Django 4.1.7 on 2023-03-01 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='categories',
            field=models.ManyToManyField(help_text='Related categories', related_name='brands', to='api.category'),
        ),
    ]
