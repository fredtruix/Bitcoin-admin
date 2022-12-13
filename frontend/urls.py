from django.urls import path
from .views import (Dashboard, registerView, LoginView,
                    LogoutView, createUserView, BitcoinAddressView, 
                    AlladddressView, StaffView, CountsView)


urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('createuser/', createUserView.as_view(), name="createuser"),
    path('address/', AlladddressView.as_view(), name="address"),
    path('staffs/', StaffView.as_view(), name="staffs"),
    path('counts/', CountsView.as_view(), name="counts"),
    path('btc-address/', BitcoinAddressView.as_view(), name="btc-address"),
    path('register/', registerView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
]
