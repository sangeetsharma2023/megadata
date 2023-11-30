from django import forms
from .models import FileInfo, IssueLetter, Sender, Received, Matter,LetterFlow
from django.forms.widgets import Select, TextInput
from ckeditor.widgets import CKEditorWidget  # Import CKEditorWidget

class DateInput(forms.DateInput):
    input_type = 'date'
    format = '%d-%m-%Y'

class FileInfoForm(forms.ModelForm):
    class Meta:
        model = FileInfo
        fields = ['FileSl','FileType', 'FileName', 'FileNo', 'ActiveStatus', 'OpenDate', 'CloseDate', 'RelatedOffice', 'FileLocation', 'WordFile']

        widgets = {
            'OpenDate': DateInput(),
            'CloseDate': DateInput(),
            'FileType': forms.Select(attrs={'class': 'form-select'}),
            'FileName': forms.TextInput(attrs={'class': 'form-control'}),
            'FileNo': forms.TextInput(attrs={'class': 'form-control'}),
            'ActiveStatus': forms.Select(attrs={'class': 'form-select'}),
            'RelatedOffice': forms.TextInput(attrs={'class': 'form-control'}),
            'FileLocation': forms.TextInput(attrs={'class': 'form-control'}),
            'WordFile': forms.FileInput(attrs={'class': 'form-control'}),
        }

class SenderForm(forms.ModelForm):
    class Meta:
        model = Sender
        fields = '__all__'
        widgets = {
            'SenderShortName': forms.TextInput(attrs={'class': 'form-control'}),
            'SenderPost': forms.TextInput(attrs={'class': 'form-control'}),
            'SenderOffice': forms.TextInput(attrs={'class': 'form-control'}),
            'SenderPlace': forms.TextInput(attrs={'class': 'form-control'}),
            'SenderShortNameH': forms.TextInput(attrs={'class': 'form-control'}),
            'SenderPostH': forms.TextInput(attrs={'class': 'form-control'}),
            'SenderOfficeH': forms.TextInput(attrs={'class': 'form-control'}),
            'SenderPlaceH': forms.TextInput(attrs={'class': 'form-control'}),
            'Pincode': forms.TextInput(attrs={'class': 'form-control'}),
            'OfficeDefault': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ReceivedForm(forms.ModelForm):
    class Meta:
        model = Received
        fields = ['ReceiveDate', 'Sender', 'LetterNo', 'LetterDate', 'Urgency', 'DueDate', 'ReceiveStatus', 'LetterSubject', 'LetterDetail']

        widgets = {
            'ReceiveDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'format': 'dd-mm-yyyy'}),
            'Sender': forms.Select(attrs={'class': 'form-select'}),
            'LetterNo': forms.TextInput(attrs={'class': 'form-control'}),
            'LetterDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'format': 'dd-mm-yyyy'}),
            'Urgency': forms.Select(attrs={'class': 'form-select'}),
            'DueDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'format': 'dd-mm-yyyy'}),
            'ReceiveStatus': forms.Select(attrs={'class': 'form-select'}),
            'LetterSubject': forms.TextInput(attrs={'class': 'form-control'}),
            'LetterDetail': CKEditorWidget(),  # Use CKEditorWidget for rich text editing
        }

class MatterForm(forms.ModelForm):
    class Meta:
        model = Matter
        fields = ['FileId', 'MatterType', 'MatterStatus']

        widgets = {
            'FileId': forms.Select(attrs={'class': 'form-select'}),
            'MatterType': forms.Select(attrs={'class': 'form-select'}),
            'MatterStatus': forms.Select(attrs={'class': 'form-select'}),
            # Add other fields as needed
        }

class ReceivedExistingMatterForm(forms.ModelForm):
    class Meta:
        model = Received
        fields = ['MatterId', 'ReceiveDate', 'Sender', 'LetterNo', 'LetterDate', 'Urgency', 'DueDate', 'ReceiveStatus', 'LetterSubject', 'LetterDetail']

        widgets = {
            'MatterId': forms.Select(attrs={'class': 'form-select'}),
            'ReceiveDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'format': 'dd-mm-yyyy'}),
            'Sender': forms.Select(attrs={'class': 'form-select'}),
            'LetterNo': forms.TextInput(attrs={'class': 'form-control'}),
            'LetterDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'format': 'dd-mm-yyyy'}),
            'Urgency': forms.Select(attrs={'class': 'form-select'}),
            'DueDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'format': 'dd-mm-yyyy'}),
            'ReceiveStatus': forms.Select(attrs={'class': 'form-select'}),
            'LetterSubject': forms.TextInput(attrs={'class': 'form-control'}),
            'LetterDetail': CKEditorWidget(),  # Use CKEditorWidget for rich text editing
        }

class CreateFlowForm(forms.ModelForm):
    class Meta:
        model = LetterFlow
        fields = ['ReceiveId', 'FlowType', 'TempFile', 'NotingText', 'Remark']

    def __init__(self, *args, **kwargs):
        super(CreateFlowForm, self).__init__(*args, **kwargs)

        # Customize the widget for LetterId based on FlowType
        self.fields['LetterId'] = forms.ModelChoiceField(
            queryset=self.get_letter_id_queryset(),
            required=False,
            widget=ConditionalLetterIdWidget(attrs={'class': 'form-select'}),
        )

    def get_letter_id_queryset(self):
        # Implement your logic to get the queryset for LetterId based on FlowType
        # Example: return IssueLetter.objects.filter(...) or any custom logic
        return IssueLetter.objects.none()


class ConditionalLetterIdWidget(Select):
    def render_options(self, *args, **kwargs):
        # Override render_options to add conditional logic for LetterId options
        # You can customize this method based on your requirements
        # Example: Filter options based on FlowType
        letter_id_queryset = self.choices.queryset
        # Add your logic here to customize options based on FlowType
        # ...

        return super().render_options(*args, **kwargs)
    
class VerifyFlowForm(forms.ModelForm):
    class Meta:
        model = LetterFlow
        exclude = ['id', 'FlowStartTimeStamp', 'FlowEndTimeStamp', 'TimeTaken', 'created_at', 'updated_at']

    def __init__(self, *args, **kwargs):
        super(VerifyFlowForm, self).__init__(*args, **kwargs)
        self.fields['ReceiveId'].widget.attrs['readonly'] = True