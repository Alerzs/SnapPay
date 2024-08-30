from django.urls import path
from payment.views import my_copun , start_trans , add_copun, CuponDetail, CuponModifier

urlpatterns = [
    path("my_copun/<str:email>" ,my_copun),
    path("trans/<str:dargah>/<str:fac_id>" , start_trans),
    path("add_copun/<str:transID>/<str:email>/<str:code>" , add_copun),
    path("detail-cupun", CuponDetail.as_view()),
    path("modify_cupom/<int:pk>", CuponModifier.as_view())

]