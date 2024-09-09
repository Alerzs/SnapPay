from django.http.response import HttpResponse , JsonResponse
from payment.models import Factor ,Copun ,Transaction ,User
from random import randint
import requests
from rest_framework.exceptions import ValidationError , PermissionDenied
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView , UpdateAPIView ,CreateAPIView ,ListAPIView
from .serialize import CopunSerializer , TransactionSerializer , Factorserialize
from rest_framework.permissions import IsAuthenticated , IsAdminUser ,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
import json


class Login(TokenObtainPairView):
    pass

class refresh(TokenRefreshView):
    pass


class CopunView(ListCreateAPIView):
    """
    shows users copun with GET method and creat a new copun with admin permisioon and POST method
    """
    queryset = Copun.objects.all()
    serializer_class = CopunSerializer

    def get_queryset(self):
        return Copun.objects.filter(user = self.request.user)
    
    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = [IsAdminUser]
        elif self.request.method == 'GET':
            self.permission_classes = [IsAuthenticated]
        return super(CopunView , self).get_permissions()
    

class CopunEditor(RetrieveUpdateDestroyAPIView):
    """
    edit or delete a copun needs admin permision
    """
    queryset = Copun.objects.all()
    serializer_class = CopunSerializer
    permission_classes = [IsAdminUser]


class AddCopunToFactor(UpdateAPIView):
    """
    adds a new copun to user factor by updating discount_price field in factor object
    this class needs a PATCH request with "copun_code" in its body\n
    request.PATCH{
        "copun_code":"1fewf4f6"
    }
    """
    queryset = Factor.objects.all()
    serializer_class = Factorserialize
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        my_factor = serializer.instance
        coupon_code = self.request.data.get('copun_code')

        if not coupon_code:
            raise ValidationError("copun_code field is missing")
        if my_factor.user != self.request.user:
            raise PermissionDenied("this factor is not yours")

        try:
            my_coupon = Copun.objects.get(code=coupon_code)
        except Copun.DoesNotExist:
            raise ValidationError("Invalid coupon code.")  
          
        if not my_coupon.activation_status:
            raise ValidationError("copun is expired")
        for user in my_coupon.user.all():
            if user == self.request.user:
                break
        else:
            raise PermissionDenied("this copun is not active on your account")

        discount = my_coupon.percent / 100
        my_factor.discount_price = my_factor.price * (1 - discount)
        my_factor.copun = my_coupon
        serializer.save()

        return super().perform_update(serializer)

class MyFactors(ListAPIView):
    """
    returns users factors history
    """
    queryset = Factor.objects.all()
    serializer_class = Factorserialize
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Factor.objects.filter(user = self.request.user)


class StartTransaction(CreateAPIView):
    """
    creates a transaction abject by taking dargah and factors pk
    and changes the factor status to true which means the factor is paid and prevents paying a factor multiple times 
    """
    queryset = Transaction
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        data = self.request.data
        my_factor = Factor.objects.get(id = data['factor'])
        if my_factor.user != self.request.user:
            raise PermissionDenied("factor is not yours")
        if my_factor.status == True:
            raise ValidationError("this factor has already been paid")
        my_factor.status = True
        my_factor.save()
        return serializer.save(trans_id = randint(10000,99999))


class MyTrans(ListAPIView):
    """
    returns users transaction history
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Transaction.objects.filter(factor__user = self.request.user)



def get_orders(request):
    """
    send an api to get order and user object from arshia and makes factor and user objects
    """
    url = ""
    api_key = ""
    response = requests.get(url , headers={"Api-Key": api_key})
    User.objects.create()
    Factor.objects.create()



def check_pro(request):
    """
    send an api to check if user is pro or not
    """
    my_user = ""
    url = ""
    api_key = ""
    response = requests.get(url , headers={"Api-Key": api_key})
    if json.loads(response)["stat"]:
        my_factor = Factor.objects.get(user = my_user)
        my_factor.price *= 0.15
        my_factor.save()
    