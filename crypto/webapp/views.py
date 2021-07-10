from django.db.models import Case, When, Value, FloatField, F
from rest_framework import status, viewsets, permissions, filters, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *
# Create your views here.


class CoinViewSet(viewsets.ModelViewSet):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserCoinViewSet(viewsets.ModelViewSet):
    queryset = UserCoin.objects.all()
    serializer_class = UserCoinSerializer
    permission_classes = [permissions.IsAuthenticated]


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        serializer = TransactionSerializer(data=request.data)
        serializer.is_valid()
        transaction = serializer.save()
        sell_coin = UserCoin.objects.filter(coin=transaction.sell_coin, user=transaction.user).first()
        buy_coin = UserCoin.objects.filter(coin=transaction.buy_coin, user=transaction.user).first()
        if not sell_coin:
            sell_coin = UserCoin.objects.create(coin=transaction.sell_coin, user=transaction.user, avg_buying_price=0, balance=0)
        if not buy_coin:
            buy_coin = UserCoin.objects.create(coin=transaction.buy_coin, user=transaction.user, avg_buying_price=0, balance=0)
        buy_coin.avg_buying_price = (buy_coin.avg_buying_price * buy_coin.balance + transaction.value_per_coin_inr*transaction.buy_amount)/(buy_coin.balance+transaction.buy_amount)
        buy_coin.balance = buy_coin.balance + transaction.buy_amount
        sell_coin.balance = sell_coin.balance - transaction.sell_amount
        buy_coin.save()
        sell_coin.save()

        return Response(serializer.data)


class P2PViewSet(viewsets.ModelViewSet):
    queryset = P2P.objects.all()
    serializer_class = P2PSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request):
        serializer = P2PSerializer(data=request.data)
        serializer.is_valid()
        if not serializer.is_valid():
            return Response(serializer.errors)
        P2P = serializer.save()

        if P2P.coin.name == "INR":
            P2P.network_fee = P2P.amount*0.0177
            P2P.save()
        elif P2P.coin.name == "USDT":
            P2P.network_fee = P2P.amount_in_inr - P2P.amount*P2P.value_per_coin_inr
            P2P.save()
        coin = UserCoin.objects.filter(coin=P2P.coin, user=P2P.user).first()
        if not coin:
            coin = UserCoin.objects.create(coin=P2P.coin, user=P2P.user, avg_buying_price=0, balance=0)
        if coin.coin.name != "INR":
            coin.avg_buying_price = (coin.avg_buying_price*coin.balance + P2P.value_per_coin_inr*P2P.amount)/(coin.balance+P2P.amount)
        coin.balance = coin.balance + P2P.amount
        coin.save()

        return Response(serializer.data)

    @action(detail=False, methods=["get"])
    def total_invested(self, request, pk=None, *args, **kwargs):
        invested_inr = list(P2P.objects.annotate(total=Case(
            When(coin__name="INR", then=F('amount_in_inr') + F('network_fee')),
            When(coin__name="USDT", then='amount_in_inr'),
            default=Value('0'),
            output_field=FloatField()
            ),
        ).values_list('total', flat=True))

        total_network_fee = list(P2P.objects.all().values_list('network_fee', flat=True))

        return Response({"total_invested": round(sum(invested_inr), 2), "total_network_fee": round(sum(total_network_fee), 2),
                         "net_invested": round(sum(invested_inr) - sum(total_network_fee), 2)})




