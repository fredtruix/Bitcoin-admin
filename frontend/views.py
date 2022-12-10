from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegisterFrom
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.



class Dashboard(View):
    template_name = "frontend/index.html"


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



class registerView(View):
    template_name = "frontend/register_login.html"


    def get(self, request, *args, **kwargs):
        form = UserRegisterFrom()
        context = {
            "form":form,
            "register":"register"
        }
        return render(request, self.template_name, context )



    def post(self, request, *args, **kwargs):
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        return render(request, self.template_name, {"user":user} )



class LoginView(View):
    template_name = "frontend/register_login.html"  

    def get(self, request, *args, **kwargs) -> render:
      
        return render(request, self.template_name)



    def post(self, request, *args, **kwargs) -> render:
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist")
        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        return render(request, self.template_name)
