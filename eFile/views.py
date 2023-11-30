# eFile/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import CorrStatus, Received, IssueLetter, Matter,MatterStatus, LetterFlow, ReceiveFlowStatus,FlowType
from .forms import ReceivedForm, IssueLetterForm, MatterForm, VerifyForm,FlowStatusEntryForm,FlowStatusVerifyForm
from .forms import ActionForm, VerifyForm
from django.http import JsonResponse
def home(request):
    return render(request, 'eFile/home.html')

def received_list(request):
    received_items = Received.objects.all()
    return render(request, 'eFile/received_list.html', {'received_items': received_items})

# def received_detail(request, pk):
#     received_item = get_object_or_404(Received, pk=pk)
#     return render(request, 'eFile/received_detail.html', {'received_item': received_item})

def received_add(request):
    if request.method == 'POST':
        form = ReceivedForm(request.POST)
        if form.is_valid():
            received_item = form.save()
            return redirect('received_add')
    else:
        form = ReceivedForm()
    return render(request, 'eFile/received_add.html', {'form': form})

def received_edit(request, pk):
    received_item = get_object_or_404(Received, pk=pk)
    if request.method == 'POST':
        form = ReceivedForm(request.POST, instance=received_item)
        if form.is_valid():
            received_item = form.save()
            return redirect('received_list')
    else:
        form = ReceivedForm(instance=received_item)
    return render(request, 'eFile/received_edit.html', {'form': form, 'received_item': received_item})

def received_delete(request, pk):
    received_item = get_object_or_404(Received, pk=pk)
    if request.method == 'POST':
        received_item.delete()
        return redirect('received_list')
    return render(request, 'eFile/received_delete.html', {'received_item': received_item})

def get_received_details(request, received_id):
    try:
        received = Received.objects.get(pk=received_id)
        data = {
            'ReceivedDate': str(received.ReceivedDate),
            'LetterSubject': received.LetterSubject,
            'LetterDetail': received.LetterDetail,
        }
        return JsonResponse(data)
    except Received.DoesNotExist:
        return JsonResponse({'error': 'Received item not found'}, status=404)



# code for Issue Letter
def issue_letter_list(request):
    issue_letter = IssueLetter.objects.all()
    return render(request, 'eFile/issue_letter_list.html', {'issue_letter': issue_letter})

def issue_letter_detail(request, pk):
    issue_letter = get_object_or_404(IssueLetter, pk=pk)
    return render(request, 'eFile/issue_letter_detail.html', {'issue_letter': issue_letter})

def issue_letter_add(request):
    if request.method == 'POST':
        form = IssueLetterForm(request.POST)
        if form.is_valid():
            issue_letter = form.save()
            return redirect('issue_letter_detail', pk=issue_letter.pk)
    else:
        form = IssueLetterForm()
    return render(request, 'eFile/issue_letter_add.html', {'form': form})

def issue_letter_edit(request, pk):
    issue_letter = get_object_or_404(IssueLetter, pk=pk)
    if request.method == 'POST':
        form = IssueLetterForm(request.POST, instance=issue_letter)
        if form.is_valid():
            issue_letter = form.save()
            return redirect('issue_letter_detail', pk=issue_letter.pk)
    else:
        form = IssueLetterForm(instance=issue_letter)
    return render(request, 'eFile/issue_letter_edit.html', {'form': form, 'issue_letter': issue_letter})

def issue_letter_delete(request, pk):
    issue_letter = get_object_or_404(IssueLetter, pk=pk)
    if request.method == 'POST':
        issue_letter.delete()
        return redirect('issue_letter_list')
    return render(request, 'eFile/issue_letter_delete.html', {'issue_letter': issue_letter})


#Matter views


def matter_add(request):
    # Fetch all received items
    all_received_items = Received.objects.all()

    if request.method == 'POST':
        form = MatterForm(request.POST)
        if form.is_valid():
            matter = form.save()
            return redirect('matter_add')
    else:
        form = MatterForm()
    return render(request, 'matter_add.html', {'form': form})


def matter_detail(request, pk):
    matter = get_object_or_404(Matter, pk=pk)
    return render(request, 'eFile/matter_detail.html', {'matter': matter})

def matter_list(request):
    matters = Matter.objects.all()

    # Filter by MatterStatus if selected in the form
    matter_status_filter = request.GET.get('matter_status_filter')
    if matter_status_filter:
        matters = matters.filter(MatterStatus__MatterStatus=matter_status_filter)

    matter_statuses = MatterStatus.objects.all()

    return render(request, 'eFile/matter_list.html', {'matters': matters, 'matter_statuses': matter_statuses, 'selected_matter_status': matter_status_filter})
def matter_edit(request, pk):
    matter = get_object_or_404(Matter, pk=pk)
    if request.method == 'POST':
        form = MatterForm(request.POST, instance=matter)
        if form.is_valid():
            matter = form.save()
            return redirect('matter_list')
    else:
        form = MatterForm(instance=matter)
    return render(request, 'eFile/matter_edit.html', {'form': form, 'matter': matter})

def matter_delete(request, pk):
    matter = get_object_or_404(Matter, pk=pk)
    if request.method == 'POST':
        matter.delete()
        return redirect('matter_list')
    return render(request, 'eFile/matter_delete.html', {'matter': matter})

def matter_detail_with_corr(request, pk):
    matter = get_object_or_404(Matter, pk=pk)
    matter_corr_entries = MatterCorr.objects.filter(MatterId=matter)

    return render(request, 'eFile/matter_detail_with_corr.html', {'matter': matter, 'matter_corr_entries': matter_corr_entries})

# matter corr
# eFile/views.py

from .models import MatterCorr
from .forms import MatterCorrForm

def mattercorr_list(request):
    mattercorrs = MatterCorr.objects.all()
    return render(request, 'eFile/mattercorr_list.html', {'mattercorrs': mattercorrs})

def mattercorr_detail(request, pk):
    mattercorr = get_object_or_404(MatterCorr, pk=pk)
    return render(request, 'eFile/mattercorr_detail.html', {'mattercorr': mattercorr})

def mattercorr_add(request):
    form = MatterCorrForm()

    if request.method == 'POST':
        form = MatterCorrForm(request.POST)

        if form.is_valid():
            mattercorr = form.save()
            return redirect('mattercorr_detail', pk=mattercorr.pk)

    return render(request, 'eFile/mattercorr_add.html', {'form': form})

def mattercorr_edit(request, pk):
    mattercorr = get_object_or_404(MatterCorr, pk=pk)
    form = MatterCorrForm(instance=mattercorr)

    if request.method == 'POST':
        form = MatterCorrForm(request.POST, instance=mattercorr)

        if form.is_valid():
            mattercorr = form.save()
            return redirect('mattercorr_detail', pk=mattercorr.pk)

    return render(request, 'eFile/mattercorr_edit.html', {'form': form, 'mattercorr': mattercorr})

def mattercorr_delete(request, pk):
    mattercorr = get_object_or_404(MatterCorr, pk=pk)

    if request.method == 'POST':
        mattercorr.delete()
        return redirect('mattercorr_list')

    return render(request, 'eFile/mattercorr_delete.html', {'mattercorr': mattercorr})

def mattercorr_add_with_matter(request, matter_id):
    matter = get_object_or_404(Matter, pk=matter_id)

    if request.method == 'POST':
        form = MatterCorrForm(request.POST)
        if form.is_valid():
            mattercorr = form.save(commit=False)
            mattercorr.Matter = matter  # Assign the Matter object to MatterCorr
            mattercorr.save()
            return redirect('matter_detail_with_corr', pk=matter.pk)
    else:
        initial_data = {
            'MatterId': matter.pk,
            
        }
        form = MatterCorrForm(initial=initial_data)

    return render(request, 'eFile/mattercorr_add_with_matter.html', {'form': form, 'matter': matter})


#letter flow
def create_flow(request, receive_id):
    if request.method == 'POST':
        form = VerifyForm(request.POST, request.FILES)
        if form.is_valid():
            flow = form.save(commit=False)
            flow.ReceiveId_id = receive_id
            flow.save()
            return redirect('flow_detail', pk=flow.pk)  # Redirect to flow detail view
    else:
        form = VerifyForm()

    return render(request, 'eFile/create_flow.html', {'form': form})

def received_list_with_status(request):
    # Fetch unique values of Status from ReceiveFlowStatus
    corr_statuses = CorrStatus.objects.all()
    for status in corr_statuses:
        print(status)

    # Create a dictionary to store Received instances for each status
    received_dict = {}
    for status in corr_statuses:
        received_dict[status] = Received.objects.filter(receiveflowstatus__Status=status)
        

    context = {
        'statuses': corr_statuses,
        'received_dict': received_dict,
    }

    return render(request, 'eFile/received_list_with_status.html', context)

def create_letter_flow(request, received_id):
    received = get_object_or_404(Received, pk=received_id)
    if request.method == 'POST':
        form = VerifyForm(request.POST)
        if form.is_valid():
            letter_flow = form.save(commit=False)
            letter_flow.ReceiveId = received
            # Set other fields as needed
            letter_flow.save()
            return redirect('received_list_with_status')
    else:
        form = VerifyForm()

    context = {
        'form': form,
        'received': received,
    }
    return render(request, 'eFile/create_letter_flow.html', context)

def verify_received(request, received_id):
    # Implement the logic for verifying received here
    received = get_object_or_404(Received, pk=received_id)
    return render(request, 'eFile/verify_received.html', {'received': received})

def letter_flow_detail(request, pk):
    letter_flow = get_object_or_404(LetterFlow, pk=pk)
    return render(request, 'letter_flow_detail.html', {'letter_flow': letter_flow})

def letter_flow_list_by_received(request, received_id):
    letter_flows = LetterFlow.objects.filter(ReceiveId=received_id)
    context = {'letter_flows': letter_flows, 'received_id': received_id}
    return render(request, 'eFile/letter_flow_list_by_received.html', context)

from .models import Received, ReceiveFlowStatus, Matter, MatterCorr, CorrStatus

def report_received_all(request):
    status_filter_values = Received.objects.values_list('Status', flat=True).distinct()
    # Exclude 'Letter Issued' from default filter
    default_filter_values = [value for value in status_filter_values if value != 'Letter Issued']

    received_list = Received.objects.all()

    return render(request, 'eFile/report_received_all.html', {
        'received_list': received_list,
        'status_filter_values': status_filter_values,
        'default_filter_values': default_filter_values,
    })

def action_view(request, receive_id):
    received_instance = get_object_or_404(Received, pk=receive_id)

    # Assuming you have a default FlowType or some logic to determine the appropriate FlowType
    default_flow_type = FlowType.objects.first()  # You may need to adjust this based on your model

    # Create a new LetterFlow instance for the action with a valid FlowType
    letter_flow = LetterFlow.objects.create(ReceiveId=received_instance, FlowType=default_flow_type)
    
    form = ActionForm(instance=letter_flow)
    
    if request.method == 'POST':
        form = ActionForm(request.POST, instance=letter_flow)
        if form.is_valid():
            # Process form data
            form.save()
            # Redirect or render a success message
            # Update the Received instance status
            update_received_status(receive_id, 'NewStatus')

    return render(request, 'eFile/action_form.html', {'form': form})

def verify_view(request, receive_id):
    letter_flow = get_object_or_404(LetterFlow, pk=receive_id)
    form = VerifyForm(instance=letter_flow)
    
    if request.method == 'POST':
        form = VerifyForm(request.POST, instance=letter_flow)
        if form.is_valid():
            # Process form data 
            form.save()
            # Update the Received instance status
            update_received_status(receive_id, 'AnotherStatus')
            return redirect('report_received_all')

    return render(request, 'eFile/verify_form.html', {'form': form})

def update_received_status(received_id, new_status):
    received_instance = get_object_or_404(Received, pk=received_id)
    received_instance.Status = new_status
    received_instance.save()

    return f'Status updated to {new_status} for Received ID {received_id}'



