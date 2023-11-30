from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(MatterType)
admin.site.register(Matter)
admin.site.register(Received)
admin.site.register(Sender)
admin.site.register(LetterFlow)
admin.site.register(IssueLetter)
