from django.contrib import admin
from webapp import models

# Register your models here.
admin.site.register(models.Coin)
# admin.site.register(models.Trade)
admin.site.register(models.P2P)

class TradeAdmin(admin.ModelAdmin):
    list_display = ('user', 'buy_coin', 'sell_coin', 'loss_or_gain', )

class UserCoinAdmin(admin.ModelAdmin):
    list_display = ('user', 'coin', 'avg_buying_price', 'balance', )

admin.site.register(models.Trade, TradeAdmin)
admin.site.register(models.UserCoin, UserCoinAdmin)
admin.site.register(models.File)
