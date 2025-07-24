from django.contrib import admin
from .models import Person, Donation, Stock, Receive

# Register your models here.
admin.site.register(Person)
admin.site.register(Donation)
admin.site.register(Stock)
admin.site.register(Receive)
