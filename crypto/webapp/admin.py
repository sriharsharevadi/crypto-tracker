from django.contrib import admin
from webapp import models

# Register your models here.
admin.site.register(models.Coin)
admin.site.register(models.UserCoin)
admin.site.register(models.Transaction)
admin.site.register(models.P2P)
