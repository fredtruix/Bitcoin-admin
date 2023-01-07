from django.urls import path
from .views import (Dashboard, registerView, LoginView,
                    LogoutView, createUserView, BitcoinAddressView, TransactionView,
                    AlladddressView, StaffView, CountsView, DetailView, AddressView,  BalanceView, comfirmView)


urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('createuser/', createUserView.as_view(), name="createuser"),
    path('address/', AlladddressView.as_view(), name="address"),
    path('addview/', AddressView.as_view(), name="addview"),
    path('staffs/', StaffView.as_view(), name="staffs"),
    path('counts/', CountsView.as_view(), name="counts"),
    path('detail/<str:fullName>/', DetailView.as_view(), name="detail"),
    path('balance/<str:name>/', BalanceView.as_view(), name="balance"),
    path('transactions/<str:name>/', TransactionView.as_view(), name="transactions"),
    path('confirm/<str:name>/', comfirmView.as_view(), name="confirm"),
    path('btc-address/', BitcoinAddressView.as_view(), name="btc-address"),
    path('register/', registerView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
]
