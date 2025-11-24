
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from Users.models import User
from .models import Clients, Message, Mailing

admin.site.register(Clients)
admin.site.register(Message)
admin.site.register(Mailing)
admin.site.register(User, UserAdmin)

