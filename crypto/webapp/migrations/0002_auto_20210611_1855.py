# Generated by Django 3.2.4 on 2021-06-11 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='p2p',
            name='coin',
        ),
        migrations.RemoveField(
            model_name='p2p',
            name='user',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='buy_coin',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='sell_coin',
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='user',
        ),
        migrations.RemoveField(
            model_name='usercoin',
            name='coin',
        ),
        migrations.RemoveField(
            model_name='usercoin',
            name='user',
        ),
        migrations.DeleteModel(
            name='Coin',
        ),
        migrations.DeleteModel(
            name='P2P',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='UserCoin',
        ),
    ]
