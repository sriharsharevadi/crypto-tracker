from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User
from django.db.models import Choices


class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Coin(TimeStampModel):
    name = models.CharField(max_length=20)
    wazirx_name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class UserCoin(TimeStampModel):
    coin = models.ForeignKey(Coin, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    balance = models.FloatField(default=0.0)
    avg_buying_price = models.FloatField(default=0.0)

    def __str__(self):
        return self.user.username + "_" + self.coin.name


class Transaction(TimeStampModel):
    buy_coin = models.ForeignKey(Coin, related_name="buy_coin", on_delete=models.PROTECT)
    sell_coin = models.ForeignKey(Coin, related_name="sell_coin", on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    buy_amount = models.FloatField()
    sell_amount = models.FloatField()
    value_per_coin_inr = models.FloatField()
    network_fee = models.FloatField()
    time = models.DateTimeField()
    loss_or_gain = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.user.username + " " + self.buy_coin.name + "/" + self.sell_coin.name


class P2P(TimeStampModel):
    P2P_CHOICES = [
        ('d', 'DEPOSIT'),
        ('w', 'WITHDRAW'),
    ]
    type = models.CharField(
        max_length=1,
        choices=P2P_CHOICES,
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    coin = models.ForeignKey(Coin, on_delete=models.PROTECT)
    amount = models.FloatField()
    amount_in_inr = models.FloatField(null=True, blank=True)
    value_per_coin_inr = models.FloatField(null=True,blank=True)
    network_fee = models.FloatField(null=True, blank=True)
    time = models.DateTimeField()

    def clean(self):
        if self.coin.name not in ["INR", "USDT"]:
            raise ValidationError("Coin must be INR or USDT")

    def __str__(self):
        return self.user.username + "_" + self.coin.name
