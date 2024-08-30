from django.http.response import HttpResponse , JsonResponse
from payment.models import Factor ,Copun ,Transaction ,Usr
from random import randint
from rest_framework.generics import ListAPIView, RetrieveAPIView , CreateAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serialize import CopunSerializer , Transcreate , Factorserialize
from rest_framework.permissions import IsAuthenticated
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


class TransDetail(ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = Transcreate
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class TransModifier(RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = Transcreate
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
    
class CreatFactor(CreateAPIView):
    queryset = Factor.objects.all()
    serializer_class = Factorserialize   
 
class FactorDetail(ListAPIView):
    queryset = Factor.objects.all()
    serializer_class = Factorserialize
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Factor.objects.filter(user=self.request.user)

class FactorModifier(RetrieveUpdateDestroyAPIView):
    queryset = Factor.objects.all()
    serializer_class = Factorserialize
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Factor.objects.filter(user=self.request.user)

class CreatTransaction(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = Transcreate

    
    
class CreatCopun(CreateAPIView):
    queryset = Copun.objects.all()
    serializer_class = CopunSerializer
    
class CuponDetail(ListAPIView):
    queryset = Copun.objects.all()
    serializer_class = CopunSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Copun.objects.filter(user=self.request.user)

class CuponModifier(RetrieveUpdateDestroyAPIView):
    queryset = Copun.objects.all()
    serializer_class = CopunSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Copun.objects.filter(user=self.request.user)
    