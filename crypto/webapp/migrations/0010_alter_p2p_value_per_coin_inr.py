# Generated by Django 3.2.4 on 2021-06-12 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_alter_p2p_network_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p2p',
            name='value_per_coin_inr',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
