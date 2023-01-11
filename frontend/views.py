from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import UserRegisterFrom
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from bitcoin import *
import requests
from .models import B_users, Admin_address
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
# def run():
#     i = 0
#     while i == 0:
#        print("hello")
# run()


class Dashboard(LoginRequiredMixin, View):
    template_name = "frontend/index.html"
    login_url = 'login'

    def get(self, request, *args, **kwargs) -> render:
        

        context = {
            "address": Admin_address.objects.first()
        }

        address = B_users.objects.all()
        # for i in address:
        #     if i.Btc_address:
        #         print("yes")

        return render(request, self.template_name, context)


class StaffView(LoginRequiredMixin, View):
    template_name = "frontend/staff.html"

    def get(self, request, *args, **kwargs):
        context = {
            "users": User.objects.all()
        }
        return render(request, self.template_name, context)


class CountsView(LoginRequiredMixin, View):
    template_name = "frontend/counts.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        address = Admin_address.objects.first()
        address = address.address
        response = requests.get(
            'https://chain.api.btc.com/v3/address/' + address)
        btc_address_count = B_users.objects.all().count()
        staffs = User.objects.all().count()

        context = {
            'balance': response.json(),
            "btc_count": btc_address_count,
            "staffs": staffs
        }
        return render(request, self.template_name, context)
# send()

class DetailView(LoginRequiredMixin, View):
    template_name = "frontend/detail.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        detail = B_users.objects.get(fullName=kwargs["fullName"])
        address = detail.Btc_address
        # tx_history = history("3MqUP6G1daVS5YTD8fz3QgwjZortWwxXFd")
        # print(tx_history)
        context = {
            "detail": detail
            # "details":tx_history
        }
        return render(request, self.template_name, context)


class createUserView(LoginRequiredMixin, View):
    template_name = "frontend/user.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        private_key = random_key()
        public_key = privtopub(private_key)
        address = pubkey_to_address(public_key)
        B_users.objects.create(
            fullName=request.POST.get('full_name'),
            email=request.POST.get("email"),
            phone_number=request.POST.get("phone"),
            private_key=private_key,
            public_key=public_key,
            Btc_address=address
        )
        return redirect('createuser')


class BitcoinAddressView(LoginRequiredMixin, View):
    template_name = "frontend/btc_address.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        q = request.GET.get("q")
        if q:
            context = {
                "btc_details": B_users.objects.filter(
                    Q(fullName__icontains=q) | 
                    Q(Btc_address__icontains=q) | 
                    Q(phone_number__icontains=q) |
                    Q(email__icontains=q)
                    )
            }
        else:
            context = {
                "btc_details": B_users.objects.all()
            }

        return render(request, self.template_name, context)


class AddressView(LoginRequiredMixin, View):
    template_name = "frontend/btc_address.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        context = {
            "btc_details": B_users.objects.all()[0:2]
        }
        return render(request, self.template_name, context)


class AlladddressView(LoginRequiredMixin, View):
    template_name = "frontend/alladdress.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class BalanceView(LoginRequiredMixin, View):
    template_name = "frontend/balance.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        details = B_users.objects.get(fullName=kwargs["name"])
        address = details.Btc_address
        response = requests.get(
            'https://chain.api.btc.com/v3/address/' + address)
        context = {
            "balance": response.json()
        }
        return render(request, self.template_name, context)


class comfirmView(LoginRequiredMixin, View):
    template_name = "frontend/confirm.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        details = B_users.objects.get(fullName=kwargs["name"])
        address = details.Btc_address
        balance = requests.get(
            'https://blockchain.info/q/addressbalance/' + address)
        context = {
            "balance": balance.text
        }
        return render(request, self.template_name, context)


class TransactionView(LoginRequiredMixin, View):
    template_name = "frontend/transaction.html"
    login_url = "login"

    def get(self, request, *args, **kwargs):
        details = B_users.objects.get(fullName=kwargs["name"])
        address = details.Btc_address
        response = requests.get(
            f'https://chain.api.btc.com/v3/address/bc1qgv4e5sftevns2dkku6pxgew48q6xxs3au0z4pg/tx')
        context = {
            'transactions':response.json(),
            'address': "bc1qgv4e5sftevns2dkku6pxgew48q6xxs3au0z4pg",
            # 'balance_diff':""
        }
        #  <a class="text-xs  bg-indigo-800 py-2 px-2 rounded-lg text-white font-semibold" href="{% url 'detail' btc_detail.fullName %}">View detail</a>
        return render(request, self.template_name, context)


class confirmView(LoginRequiredMixin, View):
    template_name = "frontend/confirm.html"
    login_url = "login"

    def get(self,request, *args, **kwargs) -> render:
        # args.name = kwargs["name"]
        # address = B_users.objects.get(fu)
        return render(request, self.template_name)


class registerView(View):
    template_name = "frontend/register_login.html"

    def get(self, request, *args, **kwargs) -> render:
        if request.user.is_authenticated:
            return redirect('dashboard')
        form = UserRegisterFrom()
        context = {
            "form": form,
            "register": "register"
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs) -> render or redirect:
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect('login')
        return render(request, self.template_name, {"user": user})


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
