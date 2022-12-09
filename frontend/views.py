from django.shortcuts import render
from django.views.generic import View
from .forms import UserRegisterFrom

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
            "form":form
        }
        return render(request, self.template_name, context )



    def post(self, request, *args, **kwargs):
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
        return render(request, self.template_name, {"user":user} )