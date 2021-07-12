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


# class TransactionSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Transaction
#         fields = '__all__'


class P2PSerializer(serializers.ModelSerializer):

    class Meta:
        model = P2P
        fields = '__all__'


class TradeSerializer(serializers.ModelSerializer):
    # # buy_coin = CoinSerializer(read_only=True)
    # # buy_coin_id = serializers.PrimaryKeyRelatedField(
    # #     queryset=Coin.objects.all(),
    # #     write_only=True,
    # # )
    # # sell_coin = CoinSerializer(read_only=True)
    # # sell_coin_id = serializers.PrimaryKeyRelatedField(
    # #     queryset=Coin.objects.all(),
    # #     source="sell_coin",
    # #     write_only=True,
    # # )
    # # fee_coin = CoinSerializer(read_only=True)
    # # fee_coin_id = serializers.PrimaryKeyRelatedField(
    # #     queryset=Coin.objects.all(),
    # #     source="fee_coin",
    # #     write_only=True,
    # # )
    # # buy_coin_id = serializers.SerializerMethodField()
    # # sell_coin_id = serializers.SerializerMethodField()
    # fee_currency = serializers.SerializerMethodField('is_named_bar')
    #
    # def is_named_bar(self, obj):
    #     return obj.fee_currency
    # # def get_buy_coin_id(self, obj):
    # #     if obj.market:
    # #         if obj.market.endswith('USDT'):
    # #             coin, created = Coin.objects.get_or_create(name=obj.market.replace("USDT", ""))
    # #             return coin.pk
    # #
    # # def get_sell_coin(self, obj):
    # #     if obj.market:
    # #         if obj.market.endswith('USDT'):
    # #             coin, created = Coin.objects.get_or_create(name="USDT")
    # #             return coin
    # #
    # # def get_fee_currency(self, obj):
    # #     return obj
    #
    # def validate(self, attrs):
    #     if attrs.get('market'):
    #         attrs["buy_coin"], created = Coin.objects.get_or_create(name=attrs.get('market').replace("USDT", ""))
    #         attrs["sell_coin"], created = Coin.objects.get_or_create(name="USDT")
    #     if attrs.get('fee_currency'):
    #         attrs["fee_coin"], created = Coin.objects.get_or_create(name=attrs.get('fee_currency'))
    #     return attrs
    # #
    # def create(self, validated_data):
    #     if validated_data.get('market'):
    #         validated_data["buy_coin"], created = Coin.objects.get_or_create(name=validated_data.get('market').replace("USDT", ""))
    #         validated_data["sell_coin"], created = Coin.objects.get_or_create(name="USDT")
    #     if validated_data.get('fee_currency'):
    #         validated_data["fee_coin"], created = Coin.objects.get_or_create(name=validated_data.get('fee_currency'))
    #
    #     obj = Trade.objects.create(**validated_data)
    #
    #     # obj.save(foo=validated_data['foo'])
    #     return obj
    class Meta:
        model = Trade
        fields = "__all__"
        # fields = ('market', 'volume', 'price', 'price_in_inr', 'total', 'fee', 'fee_in_inr', 'time', 'user', 'fee_currency')
        # exclude = ('buy_coin', 'sell_coin', 'fee_coin')



