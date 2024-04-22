from django.shortcuts import render
from django.views import View
from .forms import RegModelForm,LoginForm
from .models import RegModel
from django.http import HttpResponse
class Home(View):
    def get(self,request):
        return render(request,'home.html')
class RegInput(View):
    def get(self, request):
        con_dict={"rf":RegModelForm()}
        return render(request,'reginput.html',context=con_dict)
class Register(View):
    def post(self,request):
        rf1=RegModelForm(request.POST)
        if rf1.is_valid():
            rf1.save()
            return HttpResponse("Registration Successful")
class LoginInput(View):
    def get(self, request):
        con_dict={"lf":LoginForm()}
        return render(request,'logininput.html',context=con_dict)
class Login(View):
    def post(self,request):
        lf1=LoginForm(request.POST)
        if lf1.is_valid():
            qs=RegModel.objects.filter(UserName=lf1.cleaned_data["UserName"],Password=lf1.cleaned_data["Password"])
            if qs:
                return HttpResponse("Login Success")
            else:
                return HttpResponse("Login Failed")