from django.contrib.admin import register , ModelAdmin
from payment.models import Factor , Copun , Transaction , Usr


@register(Factor)
class FactorAdmin(ModelAdmin):
    list_display = [  #-----------------vaght namayesh in sooton ha ro ham neshoon mide
        'date',
        'order_id',
        'status',
        'price'
    ]
    
@register(Copun)
class CopunAdmin(ModelAdmin):
    search_fields = [
        'code',
        'percent',
        'expire_date',
    ]

@register(Transaction)
class TransactionAdmin(ModelAdmin):
    list_display = [
        'dargah',
        'copun',
        'trans_id',
        'factor'
    ]
