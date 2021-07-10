from rest_framework import serializers
from .models import *


class CoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Coin
        fields = '__all__'


class UserCoinSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserCoin
        fields = '__all__'


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'


class P2PSerializer(serializers.ModelSerializer):

    class Meta:
        model = P2P
        fields = '__all__'


