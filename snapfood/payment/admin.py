from django.contrib.admin import register , ModelAdmin
from payment.models import Factor , Copun , Transaction 

@register(Factor)
class FactorAdmin(ModelAdmin):
    list_display = [  #-----------------vaght namayesh in sooton ha ro ham neshoon mide
        'date',
        'order_id',
        'status',
        'price',
        'discount_price'
    ]
    
@register(Copun)
class CopunAdmin(ModelAdmin):
    search_fields = [
        'code',
        'percent',
        'expire_date',
        'activation_status',
    ]

@register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = [
        'dargah',
        'trans_id',
        'factor',
    ]
