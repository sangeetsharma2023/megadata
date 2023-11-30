from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import FileInfo, LetterFlow, Sender
from .forms import CreateFlowForm, FileInfoForm, SenderForm,ReceivedForm, MatterForm, ReceivedExistingMatterForm, VerifyFlowForm  # You need to create a form for your model
from django_filters.views import FilterView
from .filters import FileInfoFilter
from django.contrib import messages
# fs/views.py

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'fs/home.html'



class AddFileView(View):
    template_name = 'fs/add_file.html'

    def get(self, request):
        form = FileInfoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FileInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fs:view_file_list')
        return render(request, self.template_name, {'form': form})

class EditFileView(View):
    template_name = 'fs/edit_file.html'

    def get(self, request, file_id):
        file = get_object_or_404(FileInfo, id=file_id)
        form = FileInfoForm(instance=file)
        return render(request, self.template_name, {'form': form, 'file': file})

    def post(self, request, file_id):
        file = get_object_or_404(FileInfo, id=file_id)
        form = FileInfoForm(request.POST, instance=file)
        if form.is_valid():
            form.save()
            return redirect('fs:view_file_list')
        return render(request, self.template_name, {'form': form, 'file': file})

class DeleteFileView(View):
    template_name = 'fs/delete_file.html'

    def get(self, request, file_id):
        file = get_object_or_404(FileInfo, id=file_id)
        return render(request, self.template_name, {'file': file})

    def post(self, request, file_id):
        file = get_object_or_404(FileInfo, id=file_id)
        file.delete()
        return redirect('fs:view_file_list')

class FileListView(View):
    template_name = 'fs/view_files.html'

    def get(self, request):
        files = FileInfo.objects.all()
        return render(request, self.template_name, {'files': files})

class ViewFileView(View):
    template_name = 'fs/view_file.html'

    def get(self, request, file_id):
        file = get_object_or_404(FileInfo, id=file_id)
        return render(request, self.template_name, {'file': file})

class AddSenderView(View):
    template_name = 'fs/add_sender.html'

    def get(self, request):
        form = SenderForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SenderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('fs:sender_list')
        return render(request, self.template_name, {'form': form})


class EditSenderView(View):
    template_name = 'fs/edit_sender.html'

    def get(self, request, sender_id):
        sender = get_object_or_404(Sender, pk=sender_id)
        form = SenderForm(instance=sender)
        return render(request, self.template_name, {'form': form, 'sender': sender})

    def post(self, request, sender_id):
        sender = get_object_or_404(Sender, pk=sender_id)
        form = SenderForm(request.POST, instance=sender)
        if form.is_valid():
            form.save()
            return redirect('fs:sender_list')
        return render(request, self.template_name, {'form': form, 'sender': sender})


class DeleteSenderView(View):
    template_name = 'fs/delete_sender.html'

    def get(self, request, sender_id):
        sender = get_object_or_404(Sender, pk=sender_id)
        return render(request, self.template_name, {'sender': sender})

    def post(self, request, sender_id):
        sender = get_object_or_404(Sender, pk=sender_id)
        sender.delete()
        return redirect('fs:sender_list')


class SenderListView(View):
    template_name = 'fs/sender_list.html'

    def get(self, request):
        senders = Sender.objects.all()
        return render(request, self.template_name, {'senders': senders})


class ViewSenderView(View):
    template_name = 'fs/view_sender.html'

    def get(self, request, sender_id):
        sender = get_object_or_404(Sender, pk=sender_id)
        return render(request, self.template_name, {'sender': sender})

from django.shortcuts import render, redirect
from django.views import View
from .forms import ReceivedForm, MatterForm, ReceivedExistingMatterForm
from .models import Received, Matter

class ReceivedWithNewMatterView(View):
    template_name = 'fs/received_with_new_matter.html'

    def get(self, request, *args, **kwargs):
        received_form = ReceivedForm()
        matter_form = MatterForm()
        return render(request, self.template_name, {'received_form': received_form, 'matter_form': matter_form})

    def post(self, request, *args, **kwargs):
        received_form = ReceivedForm(request.POST)
        matter_form = MatterForm(request.POST)

        if received_form.is_valid() and matter_form.is_valid():
            # Save MatterForm
            matter = matter_form.save(commit=False)
            matter.MatterDate = received_form.cleaned_data['ReceiveDate']
            matter.MatterSubject = received_form.cleaned_data['LetterSubject']
            matter.MatterDetail = received_form.cleaned_data['LetterDetail']
            matter.save()

            # Save ReceivedForm with the new Matter
            received = received_form.save(commit=False)
            received.MatterId = matter
            received.save()

            return redirect('fs:received_list')  # Redirect to success page
        else:
            print(received_form.errors)
            print(matter_form.errors)

        return render(request, self.template_name, {'received_form': received_form, 'matter_form': matter_form})

class ReceivedWithExistingMatterView(View):
    template_name = 'fs/received_with_existing_matter.html'

    def get(self, request, *args, **kwargs):
        received_form = ReceivedExistingMatterForm()
        return render(request, self.template_name, {'received_form': received_form})

    def post(self, request, *args, **kwargs):
        received_form = ReceivedExistingMatterForm(request.POST)

        if received_form.is_valid():
            received_form.save()
            return redirect('fs:received_list')  # Redirect to success page

        return render(request, self.template_name, {'received_form': received_form})

class ReceivedListView(View):
    template_name = 'fs/received_list.html'

    def get(self, request, *args, **kwargs):
        received_list = Received.objects.all()
        return render(request, self.template_name, {'received_list': received_list})

class ReceivedEditView(View):
    template_name = 'fs/received_edit.html'

    def get(self, request, pk, *args, **kwargs):
        received_instance = get_object_or_404(Received, pk=pk)
        form = ReceivedExistingMatterForm(instance=received_instance)
        return render(request, self.template_name, {'form': form, 'pk': pk})

    def post(self, request, pk, *args, **kwargs):
        received_instance = get_object_or_404(Received, pk=pk)
        form = ReceivedExistingMatterForm(request.POST, instance=received_instance)
        if form.is_valid():
            form.save()
            return redirect('fs:received_list')
        return render(request, self.template_name, {'form': form, 'pk': pk})


class ReceivedDeleteView(View):
    template_name = 'fs/received_delete.html'

    def get(self, request, pk, *args, **kwargs):
        received_instance = get_object_or_404(Received, pk=pk)
        return render(request, self.template_name, {'received_instance': received_instance})

    def post(self, request, pk, *args, **kwargs):
        received_instance = get_object_or_404(Received, pk=pk)
        received_instance.delete()
        return redirect('fs:received_list')


class ReceivedDetailView(View):
    template_name = 'fs/received_detail.html'

    def get(self, request, pk, *args, **kwargs):
        received_instance = get_object_or_404(Received, pk=pk)
        return render(request, self.template_name, {'received_instance': received_instance})

class FileInfoListView(FilterView):
    model = FileInfo
    template_name = 'fs/file_info_list.html'
    filterset_class = FileInfoFilter

from django.http import JsonResponse

def get_file_info(request):
    matter_id = request.GET.get('matterId')

    # Replace this with your logic to fetch FileId information based on MatterId
    try:
        matter = Matter.objects.get(id=matter_id)
        file_info = {
            'fileId': matter.FileId.id,
            'fileName': matter.FileId.FileName,
            'fileType': matter.FileId.FileType,
            'activeStatus': matter.FileId.ActiveStatus,
            'fileLocation': matter.FileId.FileLocation,
            # Add other fields as needed
        }
    except Matter.DoesNotExist:
        file_info = {}

    return JsonResponse(file_info)

class CreateFlowView(View):
    template_name = 'fs/create_flow.html'

    def get(self, request, receive_id):
        form = CreateFlowForm(initial={'ReceiveId': receive_id})
        return render(request, 'fs/create_flow.html', {'form': form, 'receive_id': receive_id})


    def post(self, request, receive_id):
        form = CreateFlowForm(request.POST, initial={'ReceiveId': receive_id})

        if form.is_valid():
            # Custom logic for handling Form data before saving (if needed)
            instance = form.save(commit=False)
            # Additional logic here...

            instance.save()

            messages.success(request, 'Flow created successfully.')
            return redirect('fs:received_list')

        return render(request, 'fs/create_flow.html', {'form': form, 'receive_id': receive_id})

class AddVerifyFlowView(View):
    template_name = 'fs/add_verify_flow.html'

    def get(self, request, letter_flow_id, *args, **kwargs):
        letter_flow_instance = get_object_or_404(LetterFlow, id=letter_flow_id)
        form = VerifyFlowForm(instance=letter_flow_instance)
        return render(request, self.template_name, {'form': form, 'letter_flow_instance': letter_flow_instance, 'is_add': True})
    
    def post(self, request, letter_flow_id, *args, **kwargs):
        letter_flow_instance = get_object_or_404(LetterFlow, id=letter_flow_id)
        form = VerifyFlowForm(request.POST, instance=letter_flow_instance)
        if form.is_valid():
            form.save()
            return redirect('fs:view_verify_flows')
        return render(request, self.template_name, {'form': form, 'letter_flow_instance': letter_flow_instance, 'is_add': True})
    

class EditVerifyFlowView(View):
    template_name = 'fs/edit_verify_flow.html'

    def get(self, request, flow_id):
        flow = get_object_or_404(LetterFlow, id=flow_id)
        form = VerifyFlowForm(instance=flow)
        return render(request, self.template_name, {'form': form, 'flow': flow})

    def post(self, request, flow_id):
        flow = get_object_or_404(LetterFlow, id=flow_id)
        form = VerifyFlowForm(request.POST, instance=flow)
        if form.is_valid():
            form.save()
            return redirect('fs:view_verify_flow_list')
        return render(request, self.template_name, {'form': form, 'flow': flow})

class DeleteVerifyFlowView(View):
    template_name = 'fs/delete_verify_flow.html'

    def get(self, request, flow_id):
        flow = get_object_or_404(LetterFlow, id=flow_id)
        return render(request, self.template_name, {'flow': flow})

    def post(self, request, flow_id):
        flow = get_object_or_404(LetterFlow, id=flow_id)
        flow.delete()
        return redirect('fs:view_verify_flow_list')

class VerifyFlowListView(View):
    template_name = 'fs/view_verify_flows.html'

    def get(self, request):
        flows = LetterFlow.objects.all()
        return render(request, self.template_name, {'verify_flows': flows})
    
class LetterFlowListView(View):
    template_name = 'fs/letter_flow_list.html'

    def get(self, request, receive_id, *args, **kwargs):
        # Retrieve the Received instance based on receive_id
        received_instance = get_object_or_404(Received, pk=receive_id)

        # Filter LetterFlow entries based on ReceiveId
        letter_flows = LetterFlow.objects.filter(ReceiveId=received_instance)

        return render(request, self.template_name, {'received_instance': received_instance,'letter_flows': letter_flows})




