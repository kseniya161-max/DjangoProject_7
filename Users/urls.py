from django.urls import path
from Users.views import CreateUserView, confirm_email, CustomLoginView, CustomLogoutView
from django.contrib.auth import views as auth_views

app_name = "Users"

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('confirm/<uidb64>/<token>/', confirm_email, name='confirm_email'),
    path('login/',CustomLoginView.as_view() , name='login'),
    path('logout/', CustomLogoutView.as_view() , name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

