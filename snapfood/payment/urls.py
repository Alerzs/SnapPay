from django.urls import path
from payment.views import CopunView , CopunEditor , AddCopunToFactor , Login ,StartTransaction , MyFactors , MyTrans 

urlpatterns = [
    path("login/" ,Login.as_view()),
    path("copun/" ,CopunView.as_view()),
    path("edcopun/<int:pk>" , CopunEditor.as_view()),
    path("add_copun/<int:pk>" ,AddCopunToFactor.as_view()),
    path("trans/" ,StartTransaction.as_view()),
    path("my_factors/" ,MyFactors.as_view()),
    path("my_trans/" ,MyTrans.as_view()),
]