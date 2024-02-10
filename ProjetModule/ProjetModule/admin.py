from django.contrib import admin
from .models import Session
from .models import Response

admin.site.register(Session)
admin.site.register(Response)