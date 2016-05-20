from django.contrib import admin

# Register your models here.
from .models import Company, Debtor, Debt, Comment, Crime

admin.site.register(Company)
admin.site.register(Debtor)
admin.site.register(Debt)
admin.site.register(Comment)
admin.site.register(Crime)