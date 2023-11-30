from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Branch)
admin.site.register(CorrStatus)
admin.site.register(FileInfo)
admin.site.register(FlowType)
admin.site.register(IssueLetter)
admin.site.register(Matter)
admin.site.register(MatterStatus)
admin.site.register(MatterType)
admin.site.register(Received)
admin.site.register(Senders)
admin.site.register(MatterCorr)
admin.site.register(LetterSender)
admin.site.register(LetterFlow)
admin.site.register(LetterAttachment)
admin.site.register(ReceiveFlowStatus)



