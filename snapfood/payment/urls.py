from django.urls import path
from payment.views import my_copun , start_trans , add_copun

urlpatterns = [
    path("my_copun/<str:email>" ,my_copun),
    path("trans/<str:dargah>/<str:fac_id>" , start_trans),
    path("add_copun/<str:transID>/<str:email>/<str:code>" , add_copun),
    
]