from django.contrib import admin

from .forms import EmailForm
from .models import EmailSignUp
# Register your models here.

class AdminEmailSignUp(admin.ModelAdmin):
	list_diplay = ["__str__", "name", "email", "subject", "message"]
	form = EmailForm

admin.site.register(EmailSignUp, AdminEmailSignUp)