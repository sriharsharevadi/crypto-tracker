from datetime import datetime

from rest_framework.response import Response

from webapp.models import UserCoin
from webapp.serializers import TradeSerializer

# data = {'time': datetime.datetime(2021, 5, 30, 13, 3, 1), 'market': 'WAVESUSDT', 'price': 13.0549, 'volume': 1, 'total': 13.0549, 'trade': 'Buy', 'fee_coin': 'USDT', 'fee': 0.0261098, 'user': 1, 'price_in_inr': 1016.3892395, 'fee_in_inr': 2.032778479}
def create_trade_helper(data):
    # data = data[0]
    for d in data:
        serializer = TradeSerializer(data=d)
        serializer.is_valid()
        if not serializer.is_valid():
            return Response(serializer.errors)
        trade = serializer.save()
        fee_coin = UserCoin.objects.filter(coin=trade.fee_coin, user=trade.user).first()
        if not fee_coin:
            fee_coin = UserCoin.objects.create(coin=trade.fee_coin, user=trade.user, avg_buying_price=0, balance=0)
        fee_coin.balance = fee_coin.balance - trade.fee
        fee_coin.save()
        sell_coin = UserCoin.objects.filter(coin=trade.sell_coin, user=trade.user).first()
        buy_coin = UserCoin.objects.filter(coin=trade.buy_coin, user=trade.user).first()
        if not sell_coin:
            sell_coin = UserCoin.objects.create(coin=trade.sell_coin, user=trade.user, avg_buying_price=0, balance=0)
        if not buy_coin:
            buy_coin = UserCoin.objects.create(coin=trade.buy_coin, user=trade.user, avg_buying_price=0, balance=0)

        if trade.market.endswith('INR'):
            if buy_coin.coin.name == "INR":
                buy_coin.balance = buy_coin.balance + trade.total
                sell_coin.balance = sell_coin.balance - trade.volume
                trade.loss_or_gain = round(100*(trade.price_in_inr - sell_coin.avg_buying_price)/sell_coin.avg_buying_price, 2)
            else:
                buy_coin.avg_buying_price = (buy_coin.avg_buying_price * buy_coin.balance + trade.price_in_inr*trade.volume)/(buy_coin.balance+trade.volume)
                buy_coin.balance = buy_coin.balance + trade.volume
                sell_coin.balance = sell_coin.balance - trade.total
        elif trade.market.endswith('USDT'):
            if buy_coin.coin.name == "USDT":
                buy_coin.balance = buy_coin.balance + trade.total
                sell_coin.balance = sell_coin.balance - trade.volume
                trade.loss_or_gain = round(100*(trade.price_in_inr - sell_coin.avg_buying_price)/sell_coin.avg_buying_price, 2)
            else:
                buy_coin.avg_buying_price = (buy_coin.avg_buying_price * buy_coin.balance + trade.price_in_inr*trade.volume)/(buy_coin.balance+trade.volume)
                buy_coin.balance = buy_coin.balance + trade.volume
                sell_coin.balance = sell_coin.balance - trade.total
        elif trade.market.endswith('WRX'):
            if buy_coin.coin.name == "WRX":
                buy_coin.balance = buy_coin.balance + trade.total
                sell_coin.balance = sell_coin.balance - trade.volume
                trade.loss_or_gain = round(100*(trade.price_in_inr - sell_coin.avg_buying_price)/sell_coin.avg_buying_price, 2)
            else:
                buy_coin.avg_buying_price = (buy_coin.avg_buying_price * buy_coin.balance + trade.price_in_inr*trade.volume)/(buy_coin.balance+trade.volume)
                buy_coin.balance = buy_coin.balance + trade.volume
                sell_coin.balance = sell_coin.balance - trade.total
        else:
            print("shiiit")
        buy_coin.save()
        sell_coin.save()
        trade.save()

        # buy_coin.avg_buying_price = (buy_coin.avg_buying_price * buy_coin.balance + trade.price_in_inr*trade.volume)/(buy_coin.balance+trade.volume)
        # buy_coin.balance = buy_coin.balance + trade.volume
        # sell_coin.balance = sell_coin.balance - trade.price*trade.volume
        # buy_coin.save()
        # sell_coin.save()
        # if buy_coin.coin.name in ["INR", "USDT", "WRX", "BTC"] and sell_coin.coin.name not in ["INR", "USDT", "WRX", "BTC"]:
        #     trade.loss_or_gain = round(100*(trade.price_in_inr - sell_coin.avg_buying_price)/sell_coin.avg_buying_price,2)
        #     trade.save()
    # return Response(serializer.data)
    return True
