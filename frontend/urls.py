from django.urls import path
from .views import Dashboard, registerView, LoginView



urlpatterns = [
    path('dashboard/', Dashboard.as_view(), name="dashboard"),
    path('register/', registerView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name="login")
]