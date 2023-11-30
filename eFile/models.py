from django.db import models
from django.db import models
from django.db.models import ForeignKey
#from django_summernote.fields import SummernoteTextField
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Senders(models.Model):
    SenderId = models.AutoField(primary_key=True)
    SenderPost = models.CharField(max_length=100)
    SenderOffice = models.CharField(max_length=100)
    SenderPlace = models.CharField(max_length=100)
    Pincode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.SenderPost}, {self.SenderOffice}, {self.SenderPlace}-{self.Pincode}"
    
class Branch(models.Model):
    BranchId = models.AutoField(primary_key=True)
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

    FileId = models.AutoField(primary_key=True)
    FileSl = models.IntegerField(default=0)
    FileType = models.CharField(max_length=15, choices=FILE_TYPE_CHOICES)
    FileName = models.CharField(max_length=255)
    FileNo = models.CharField(max_length=50, null=True, blank=True)
    ActiveStatus = models.BooleanField(default=True)
    OpenDate = models.DateField()
    CloseDate = models.DateField(null=True, blank=True)
    RelatedOffice = models.CharField(max_length=100)
    FileLocation = models.CharField(max_length=10)
    WordFile = models.FileField(upload_to='word_files/',null=True, blank= True)

    def __str__(self):
        return f"{self.FileSl} - {self.FileName}"
    

class Received(models.Model):
    URGENCY_CHOICES = [
        ('Normal', 'Normal'),
        ('Urgent', 'Urgent'),
        ('MostUrgent', 'Most Urgent'),
    ]

    ReceiveId = models.AutoField(primary_key=True)
    ReceiveDate = models.DateField()
    Sender = models.ForeignKey(Senders, on_delete=models.CASCADE, default='1')
    LetterNo = models.CharField(max_length=50, blank=True,null=True)
    LetterDate = models.DateField()
    LetterSubject = models.CharField(max_length=255)
    LetterDetail= RichTextField(blank=True, null= True)
    # LetterDetail = models.TextField(null=True, blank=True)
    Urgency = models.CharField(max_length=15, choices=URGENCY_CHOICES)
    DueDate = models.DateField(null=True, blank=True)
    Status = models.CharField(max_length=20, default='Letter Received')

    def __str__(self):
        return f"Received on {self.ReceiveDate} - {self.LetterSubject}"

    def save(self, *args, **kwargs):
        # Save the Received instance
        super(Received, self).save(*args, **kwargs)

        # Update ReceiveFlowStatus when status is "Letter Received"
        if self.Status == "Letter Received":
            # Create or update ReceiveFlowStatus
            receive_flow_status, created = ReceiveFlowStatus.objects.get_or_create(
                ReceiveId=self,
                defaults={'Status': 'Letter Received'},
            )
            if not created:
                receive_flow_status.Status = 'Letter Received'
                receive_flow_status.save()
    

class IssueLetter(models.Model):
    URGENCY_CHOICES = [
        ('Normal', 'Normal'),
        ('Urgent', 'Urgent'),
        ('MostUrgent', 'Most Urgent'),
    ]

    LetterId = models.AutoField(primary_key=True)
    LetterDate = models.DateField(null=True, blank=True)
    LetterSubject = models.CharField(max_length=255)
    LetterText = models.TextField(null=True, blank=True)
    Urgency = models.CharField(max_length=15, choices=URGENCY_CHOICES)
    FileId = models.ForeignKey(FileInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.LetterSubject


class MatterType(models.Model):
    Id = models.AutoField(primary_key=True)
    MatterType = models.CharField(max_length=50)
    MatterDesc = models.TextField(null=True, blank= True)

    def __str__(self):
        return self.MatterType
    
class MatterStatus(models.Model):
    StatusId = models.AutoField(primary_key=True)
    MatterStatus = models.CharField(max_length=50)
    StatusDetail = models.TextField(null=True, blank= True)

    def __str__(self):
        return self.MatterStatus
    
class Matter(models.Model):
    MatterId = models.AutoField(primary_key=True)
    MatterDate = models.DateField()
    FileId = models.ForeignKey(FileInfo, on_delete=models.CASCADE)
    MatterSubject = models.CharField(max_length=255)
    MatterDetail = models.TextField(null=True, blank= True)
    MatterType = models.ForeignKey(MatterType, on_delete=models.CASCADE)
    MatterStatus = models.ForeignKey(MatterStatus, on_delete=models.CASCADE)

    def __str__(self):
        return self.MatterSubject
    
class CorrStatus(models.Model):
    CorrStatusId = models.AutoField(primary_key=True)
    CorrStatus = models.CharField(max_length=50)
    Detail = models.TextField(null=True, blank= True)

    def __str__(self):
        return self.CorrStatus
    
class MatterCorr(models.Model):
    Id = models.AutoField(primary_key=True)
    MatterId = models.ForeignKey(Matter, on_delete=models.CASCADE)
    CorrStatus = models.ForeignKey(CorrStatus, on_delete=models.CASCADE)
    ReceiveId = models.ForeignKey(Received, on_delete=models.CASCADE, null=True, blank= True)
    IssueId = models.ForeignKey(IssueLetter, on_delete=models.CASCADE,null=True, blank= True)
    Remark = models.TextField(null=True, blank= True)

    def __str__(self):
        return f"MatterCorr - {self.Id}"
    
class FlowType(models.Model):
    FlowId = models.AutoField(primary_key=True)
    FlowType = models.CharField(max_length=50)
    Remark = models.TextField(null=True, blank= True)

    def __str__(self):
        return self.FlowType
    

class LetterFlow(models.Model):
    SUPERIOR_ACTION_CHOICES = [
        ('Approved', 'Approved'),
        ('Corrected', 'Corrected'),
        ('Rejected', 'Rejected'),
    ]

    Id = models.AutoField(primary_key=True)
    ReceiveId = models.ForeignKey(Received, on_delete=models.CASCADE)
    FlowType = models.ForeignKey(FlowType, on_delete=models.CASCADE)
    TempFile = models.BooleanField(default=False)
    NotingText = RichTextField(null=True, blank= True)
    LetterId = models.ForeignKey(IssueLetter, on_delete=models.CASCADE,null=True, blank= True)
    SuperiorAction = models.CharField(max_length=15, choices=SUPERIOR_ACTION_CHOICES,null=True, blank= True)
    FlowStartTimeStamp = models.DateTimeField(default=datetime.now)
    FlowEndTimeStamp = models.DateTimeField(null=True, blank=True)
    TimeTaken = models.DurationField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.FlowEndTimeStamp is not None:
            self.TimeTaken = self.FlowEndTimeStamp - self.FlowStartTimeStamp
        super(LetterFlow, self).save(*args, **kwargs)

    def __str__(self):
        return f"LetterFlow - {self.Id}"
    
class ReceiveFlowStatus(models.Model):
    Id = models.AutoField(primary_key=True)
    ReceiveId = models.ForeignKey(Received, on_delete=models.CASCADE)
    Status = models.CharField(max_length=50)

    def save(self, *args, **kwargs):
        letter_flow = LetterFlow.objects.filter(ReceiveId=self.ReceiveId).order_by('-FlowStartTimeStamp').first()

        if letter_flow:
            status = letter_flow.FlowType.FlowType

            if letter_flow.SuperiorAction:
                status += f'-{letter_flow.SuperiorAction}'

            self.Status = status

        super(ReceiveFlowStatus, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.Status}"

class LetterSender(models.Model):
    SENDER_TYPE_CHOICES = [
        ('Sender', 'Sender'),
        ('Receiver', 'Receiver'),
        ('Copyto', 'Copy To'),
    ]

    Id = models.AutoField(primary_key=True)
    LetterId = models.ForeignKey(IssueLetter, on_delete=models.CASCADE)
    SenderType = models.CharField(max_length=15, choices=SENDER_TYPE_CHOICES)
    SenderText = models.TextField(null=True, blank= True)

    def __str__(self):
        return f"LetterSender - {self.Id}"


class LetterAttachment(models.Model):
    Id = models.AutoField(primary_key=True)
    AttachmentText = models.TextField()
    LetterId = models.ForeignKey(IssueLetter, on_delete=models.CASCADE)

    def __str__(self):
        return f"LetterAttachment - {self.Id}"
