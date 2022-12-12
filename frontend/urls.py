from django.urls import path
from .views import (Dashboard, registerView, LoginView,
                    LogoutView, createUserView, BitcoinAddressView)


urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('createuser/', createUserView.as_view(), name="createuser"),
    path('btc-address/', BitcoinAddressView.as_view(), name="btc-address"),
    path('register/', registerView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout")
]
