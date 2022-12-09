from django.shortcuts import render
from django.views.generic import View

# Create your views here.



class Dashboard(View):
    template_name = "frontend/index.html"


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



class registerView(View):
    template_name = "frontend/register_login.html"


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)



    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)