# Generated by Django 4.1.2 on 2022-10-19 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desafio2', '0008_remove_portfolio_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conhecer',
            name='video',
            field=models.CharField(max_length=300, verbose_name='Video'),
        ),
    ]
