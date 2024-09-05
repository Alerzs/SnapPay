from django.http.response import HttpResponse , JsonResponse
from payment.models import Factor ,Copun ,Transaction 
from random import randint
from rest_framework.generics import ListAPIView, RetrieveAPIView , CreateAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serialize import CopunSerializer , Transcreate , Factorserialize
from rest_framework.permissions import IsAuthenticated , IsAdminUser ,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView , token_refresh



def my_copun(request , email):
    my_copun = Copun.objects.all()
    lst = []
    for item in my_copun:
        if item.user == email:
            dic = {
                "code":item.code,
                "exp":item.expire_date
            }
        lst.append(dic)
    return JsonResponse(lst , safe=False)


def start_trans(request ,dargah ,fac_id):
    my_factor = Factor.objects.get(order_id = fac_id)
    gen_id = randint(1000000,9999999)
    my_trans = Transaction.objects.create(dargah = dargah , trans_id = gen_id , copun = None , factor = my_factor)
    return JsonResponse({
        "dargah":my_trans.dargah,
        "trans_id":my_trans.trans_id,
        "copun":my_trans.copun,
        "factor_id":my_trans.factor.order_id
    })
    


def add_copun(request , transID , email , code):
    try:
        copun = Copun.objects.get(code = code)
    except:
        return HttpResponse("invalid copun")
    if copun.user.email == email:
        my_trans = Transaction.objects.get(trans_id = transID)
        my_trans.copun = copun
        return HttpResponse("copun added successfuly")
    return HttpResponse("email is wronge")


class login(TokenObtainPairView):
    pass

class refresh(token_refresh):
    pass


class TransDetail(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = Transcreate
    def get_permissions(self):
        if self.action == 'POST':
            self.permission_classes = [IsAdminUser]
        elif self.action == 'GET':
            self.permission_classes =[AllowAny]
        return super().get_permissions()

    
 
class FactorDetail(ListCreateAPIView):
    queryset = Factor.objects.all()
    serializer_class = Factorserialize
    permission_classes = [IsAuthenticated]
    def get_permissions(self):
        if self.action == 'POST':
            self.permission_classes = [IsAdminUser]
        elif self.action == 'GET':
            self.permission_classes =[AllowAny]
        return super().get_permissions()

class FactorModifier(RetrieveUpdateDestroyAPIView):
    queryset = Factor.objects.all()
    serializer_class = Factorserialize
    permission_classes = [IsAdminUser]



    
    
    
class CuponDetail(ListCreateAPIView):
    queryset = Copun.objects.all()
    serializer_class = CopunSerializer
    def get_permissions(self):
        if self.action == 'POST':
            self.permission_classes = [IsAdminUser]
        elif self.action == 'GET':
            self.permission_classes =[AllowAny]
        return super().get_permissions()

class CuponModifier(RetrieveUpdateDestroyAPIView):
    queryset = Copun.objects.all()
    serializer_class = CopunSerializer
    permission_classes = [IsAdminUser]
    