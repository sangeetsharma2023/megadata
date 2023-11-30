from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
# Create your models here.

class Branch(models.Model):
    
    BranchName = models.CharField(max_length=50)

    def __str__(self):
        return self.BranchName

class FileInfo(models.Model):
    FILE_TYPE_CHOICES = [
        ('Corr', 'Correspondence'),
        ('Saction', 'Sanction'),
        ('L-Case', 'Legal Case'),
        ('CashConveyance', 'Cash Conveyance'),
        ('Duplicate', 'Duplicate'),
        ('DeceasedClaim', 'Deceased Claim'),
        ('CourtCase', 'Court Case'),
        ('Statement', 'Statement'),
    ]

    FILE_STATUS_ACTIVE = 'Active'
    FILE_STATUS_CLOSED = 'Closed'

    FILE_STATUS_CHOICES = [
        (FILE_STATUS_ACTIVE, 'Active'),
        (FILE_STATUS_CLOSED, 'Closed'),
    ]

    FileSl = models.IntegerField(default=0)
    FileType = models.CharField(max_length=15, choices=FILE_TYPE_CHOICES)
    FileName = models.CharField(max_length=255)
    FileNo = models.CharField(max_length=50, null=True, blank=True)
    ActiveStatus = models.CharField(max_length=10, choices=FILE_STATUS_CHOICES, default=FILE_STATUS_ACTIVE)
    OpenDate = models.DateField()
    CloseDate = models.DateField(null=True, blank=True)
    RelatedOffice = models.CharField(max_length=100)
    FileLocation = models.CharField(max_length=10)
    WordFile = models.FileField(upload_to='word_files/', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.CloseDate:
            self.ActiveStatus = self.FILE_STATUS_CLOSED
        else:
            self.ActiveStatus = self.FILE_STATUS_ACTIVE
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.FileSl} - {self.FileName}"
    
class MatterType(models.Model):
    
    MatterType = models.CharField(max_length=50)
    MatterDesc = models.TextField(null=True, blank= True)

    def __str__(self):
        return self.MatterType
    
class Matter(models.Model):

    MATTER_STATUS = [
        ('Active', 'Active'),
        ('Closed', 'Closed'),
    ]

    
    MatterDate = models.DateField()
    FileId = models.ForeignKey(FileInfo, on_delete=models.CASCADE)
    MatterSubject = models.CharField(max_length=255)
    MatterDetail = RichTextField(null=True, blank= True)
    MatterType = models.ForeignKey(MatterType, on_delete=models.CASCADE)
    MatterStatus = models.CharField(max_length=10, choices=MATTER_STATUS, default = 'Active', null = True, blank = True)

    def __str__(self):
        return self.MatterSubject

class SendersManager(models.Manager):
    def set_default_office(self, sender_instance=None):
        if sender_instance:
            # Ensure that only one entry has OfficeDefault set to True
            Sender.objects.exclude(pk=sender_instance.pk).update(OfficeDefault=False)
        else:
            # Handle the case where set_default_office is called without an instance
            Sender.objects.update(OfficeDefault=False)

class Sender(models.Model):
    SenderShortName = models.CharField(max_length=30)
    SenderPost = models.CharField(max_length=100)
    SenderOffice = models.CharField(max_length=100)
    SenderPlace = models.CharField(max_length=100)
    SenderShortNameH = models.CharField(max_length=30, null=True, blank=True)
    SenderPostH = models.CharField(max_length=100, null=True, blank=True)
    SenderOfficeH = models.CharField(max_length=100, null=True, blank=True)
    SenderPlaceH = models.CharField(max_length=100, null=True, blank=True)
    Pincode = models.CharField(max_length=6)
    OfficeDefault = models.BooleanField(default=False)

    objects = SendersManager()

    def save(self, *args, **kwargs):
        if self.OfficeDefault:
            # If this entry is set to OfficeDefault, update others
            Sender.objects.set_default_office(sender_instance=self)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.SenderPost}, {self.SenderOffice}, {self.SenderPlace}-{self.Pincode}"
    
class Received(models.Model):
    URGENCY_CHOICES = [
        ('Normal', 'Normal'),
        ('Urgent', 'Urgent'),
        ('MostUrgent', 'Most Urgent'),
    ]

    RECEIVE_STATUS_CHOICES = [
        ('Received', 'Received'),
        ('Issued', 'Issued'),
        ('Filed', 'Filed')
    ]

    FLOW_STATUS_CHOICES = [
        ('Noting Put Up', 'Noting Put Up'),
        ('Noting Rejected', 'Noting Rejected'),
        ('Noting Corrected', 'Noting Corrected'),
        ('Noting Approved', 'Noting Approved'),
        ('Draft Put Up', 'Draft Put Up'),
        ('Draft Rejected', 'Draft Rejected'),
        ('Draft Corrected', 'Draft Corrected'),
        ('Draft Approved', 'Draft Approved'),
        ('Letter Put Up', 'Letter Put Up'),
        ('Letter Rejected', 'Letter Rejected'),
        ('Letter Corrected', 'Letter Corrected'),
        ('Letter Approved', 'Letter Approved'),    

    ]
    
    ReceiveDate = models.DateField()
    Sender = models.ForeignKey(Sender, on_delete=models.CASCADE)
    LetterNo = models.CharField(max_length=50, blank=True,null=True)
    LetterDate = models.DateField()
    LetterSubject = models.CharField(max_length=255)
    LetterDetail= RichTextField(blank=True, null= True)
    # LetterDetail = models.TextField(null=True, blank=True)
    Urgency = models.CharField(max_length=15, choices=URGENCY_CHOICES)
    DueDate = models.DateField(null=True, blank=True)
    MatterId = models.ForeignKey(Matter, on_delete=models.CASCADE)
    ReceiveStatus = models.CharField(max_length=20, choices=RECEIVE_STATUS_CHOICES)
    FlowStatus = models.CharField(max_length=20, choices=FLOW_STATUS_CHOICES, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Received on {self.ReceiveDate} - {self.LetterSubject}"

    def save(self, *args, **kwargs):
        # Update the 'updated_at' field every time the model is saved
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

class IssueLetter(models.Model):
    URGENCY_CHOICES = [
        ('Normal', 'Normal'),
        ('Urgent', 'Urgent'),
        ('MostUrgent', 'Most Urgent'),
    ]

    LETTER_TYPE_CHOICES = [
        ('Draft', 'Draft'),
        ('Letter', 'Letter'),
    ]

    LETTER_STATUS_CHOICES = [
        ('Created', 'Created'),
        ('Verified', 'Verified'),
    ]

    
    LetterDate = models.DateField(null=True, blank=True)
    LetterSubject = models.CharField(max_length=255)
    LetterBody = RichTextField(null=True, blank=True)
    Urgency = models.CharField(max_length=15, choices=URGENCY_CHOICES)
    MatterId = models.ForeignKey(Matter, on_delete=models.CASCADE)
    LetterType = models.CharField(max_length=10, choices=LETTER_TYPE_CHOICES)
    LetterStatus = models.CharField(max_length=10, choices=LETTER_STATUS_CHOICES)


    def __str__(self):
        return self.LetterSubject


class LetterFlow(models.Model):
    SUPERIOR_ACTION_CHOICES = [
        ('Approved', 'Approved'),
        ('Corrected', 'Corrected'),
        ('Rejected', 'Rejected'),
    ]
    

    FLOW_TYPE_CHOICES= [
        ('Noting Put Up', 'Noting Put Up'),
        ('Draft Put Up', 'Draft Put Up'),
        ('Letter Put Up', 'Letter Put Up'),
    ]

    
    ReceiveId = models.ForeignKey(Received, on_delete=models.CASCADE)
    FlowType = models.CharField(max_length=15, choices=FLOW_TYPE_CHOICES)
    TempFile = models.BooleanField(default=False)
    NotingText = RichTextField(null=True, blank= True)
    LetterId = models.ForeignKey(IssueLetter, on_delete=models.CASCADE,null=True, blank= True)
    SuperiorAction = models.CharField(max_length=15, choices=SUPERIOR_ACTION_CHOICES,null=True, blank= True)
    Remark = models.TextField(null=True, blank=True)
    FlowStartTimeStamp = models.DateTimeField(auto_now_add=True)
    FlowEndTimeStamp = models.DateTimeField(null=True, blank=True)
    TimeTaken = models.DurationField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.FlowEndTimeStamp is not None:
            self.TimeTaken = self.FlowEndTimeStamp - self.FlowStartTimeStamp
        super(LetterFlow, self).save(*args, **kwargs)

    
        # Update the 'updated_at' field every time the model is saved
        self.updated_at = timezone.now()
        super().save(*args, **kwargs)

        # Update FlowStatus in Received model based on conditions
        received = self.ReceiveId
        if self.SuperiorAction:
            # If SuperiorAction is not blank, concat first letters of FlowType and SuperiorAction
            received.FlowStatus = f"{self.FlowType.split()[0]} {self.SuperiorAction.split()[0]}"
        else:
            # If SuperiorAction is blank, set FlowStatus based on FlowType
            received.FlowStatus = self.FlowType

        received.save()


    def __str__(self):
        return f"LetterFlow - {self.Id}"
    
