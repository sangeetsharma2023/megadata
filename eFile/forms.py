# eFile/forms.py
from django import forms
from .models import Received, IssueLetter,Matter, MatterCorr, MatterStatus
#from bootstrap_datepicker_plus import DatePickerInput
from django.contrib.admin.widgets import AdminDateWidget

class ReceivedForm(forms.ModelForm):
    class Meta:
        model = Received
        fields = '__all__'
        widgets={
            "ReceiveDate": AdminDateWidget(),
            "LetterDate": AdminDateWidget(),
            "DueDate": AdminDateWidget()
        }

        
        

class IssueLetterForm(forms.ModelForm):
    class Meta:
        model = IssueLetter
        fields = '__all__'
        
class MatterForm(forms.ModelForm):
    class Meta:
        model = Matter
        fields = '__all__'
        widgets = {
            'MatterDate': forms.DateInput(attrs={'class': 'datepicker'}),
            # Add more date fields if needed, replacing 'your_date_field_name' with the actual field name.
        }

class MatterCorrForm(forms.ModelForm):
    class Meta:
        model = MatterCorr
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(MatterCorrForm, self).__init__(*args, **kwargs)

        # Filter MatterId based on MatterStatus
        if self.instance:
            filtered_matter_status_ids = MatterStatus.objects.exclude(MatterStatus__in=['Closed', 'Filed']).values_list('StatusId', flat=True)
            filtered_matters = Matter.objects.filter(MatterStatus__in=filtered_matter_status_ids)
            self.fields['MatterId'].queryset = filtered_matters

        # # Enable either ReceiveId or IssueId based on CorrStatus
        # if self.instance and (self.instance.CorrStatus.MatterStatus == 'Letter Received' or self.instance.CorrStatus.MatterStatus == 'Letter Filed'):
        #     self.fields['IssueId'].widget.attrs['disabled'] = True
        #     self.fields['ReceiveId'].queryset = Received.objects.filter(LetterStatus__in=['Not Received', 'In Progress'])

        # elif self.instance and self.instance.CorrStatus.MatterStatus == 'Letter Issued':
        #     self.fields['ReceiveId'].widget.attrs['disabled'] = True
        #     self.fields['IssueId'].queryset = IssueLetter.objects.exclude(id__in=MatterCorr.objects.values_list('IssueId', flat=True))

        # # Set the required attribute based on CorrStatus
        # if self.instance and self.instance.CorrStatus.MatterStatus:
        #     if self.instance.CorrStatus.MatterStatus in ['Letter Received', 'Letter Filed']:
        #         self.fields['ReceiveId'].required = True
        #     elif self.instance.CorrStatus.MatterStatus == 'Letter Issued':
        #         self.fields['IssueId'].required = True