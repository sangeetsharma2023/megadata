from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(AccountHeads)
admin.site.register(ExpenseCategory)
admin.site.register(IncomeCategory)
admin.site.register(ExpenseSubCategory)
admin.site.register(Person)
admin.site.register(Transaction)
admin.site.register(ItemTag)

