from django.urls import path

from Users.views import CreateUserView, confirm_email, CustomLoginView, CustomLogoutView

app_name = "Users"

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('confirm/<uidb64>/<token>/', confirm_email, name='confirm_email'),
    path('login',CustomLoginView.as_view() , name='login'),
    path('logout', CustomLogoutView.as_view() , name='logout'),
]

