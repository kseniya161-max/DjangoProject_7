from django.urls import path

from Users.views import CreateUserView

app_name = "Users"

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('confirm/<uidb64>/<token>/', confirm_email, name='confirm_email'),
]
