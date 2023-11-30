from django import forms
from .models import FileInfo, Sender, Received, Matter
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