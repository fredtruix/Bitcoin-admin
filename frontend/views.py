from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegisterFrom
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.



class Dashboard(LoginRequiredMixin, View):
    template_name = "frontend/index.html"
    login_url = 'login'


    def get(self, request, *args, **kwargs) -> render:
        return render(request, self.template_name)


class createUserView(LoginRequiredMixin, View):
    template_name = "frontend/index.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)



class registerView( View):
    template_name = "frontend/register_login.html"


    def get(self, request, *args, **kwargs) -> render:
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = UserRegisterFrom()
        context = {
            "form":form,
            "register":"register"
        }
        return render(request, self.template_name, context )



    def post(self, request, *args, **kwargs) -> render or redirect:
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
        if request.user.is_authenticated:
            return redirect('dashboard')
      
        return render(request, self.template_name)



    def post(self, request, *args, **kwargs) -> render or redirect:
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

class LogoutView(View):

    def get(self, request, *args, **kwargs) -> redirect:
        logout(request)
        return redirect('login')
