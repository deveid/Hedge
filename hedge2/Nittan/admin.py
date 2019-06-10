from django.contrib import admin
from .models import *
from .forms import *

# Register your models here.

class YourAdmin(admin.ModelAdmin):
    def formfield_for_foreignkey(self, db_field, request, **kwargs):                
        if db_field.name == 'user': kwargs['queryset'] = User.objects.filter(user=request.user)

admin.site.register(BusinessOwner_Registration)
admin.site.register(Investor_Registration)
admin.site.register(User)
admin.site.register(ContactModel)
admin.site.register(payments)

   