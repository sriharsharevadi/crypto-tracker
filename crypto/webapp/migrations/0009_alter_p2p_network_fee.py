# Generated by Django 3.2.4 on 2021-06-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_p2p_amount_in_inr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='p2p',
            name='network_fee',
            field=models.FloatField(blank=True, null=True),
        ),
    ]