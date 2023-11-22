# eFile/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Received, IssueLetter, Matter
from .forms import ReceivedForm, IssueLetterForm, MatterForm

def home(request):
    return render(request, 'eFile/home.html')

def received_list(request):
    received_items = Received.objects.all()
    return render(request, 'eFile/received_list.html', {'received_items': received_items})

def received_detail(request, pk):
    received_item = get_object_or_404(Received, pk=pk)
    return render(request, 'eFile/received_detail.html', {'received_item': received_item})

def received_add(request):
    if request.method == 'POST':
        form = ReceivedForm(request.POST)
        if form.is_valid():
            received_item = form.save()
            return redirect('received_detail', pk=received_item.pk)
    else:
        form = ReceivedForm()
    return render(request, 'eFile/received_add.html', {'form': form})

def received_edit(request, pk):
    received_item = get_object_or_404(Received, pk=pk)
    if request.method == 'POST':
        form = ReceivedForm(request.POST, instance=received_item)
        if form.is_valid():
            received_item = form.save()
            return redirect('received_detail', pk=received_item.pk)
    else:
        form = ReceivedForm(instance=received_item)
    return render(request, 'eFile/received_edit.html', {'form': form, 'received_item': received_item})

def received_delete(request, pk):
    received_item = get_object_or_404(Received, pk=pk)
    if request.method == 'POST':
        received_item.delete()
        return redirect('received_list')
    return render(request, 'eFile/received_delete.html', {'received_item': received_item})


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


def matter_list(request):
    matters = Matter.objects.all()
    return render(request, 'eFile/matter_list.html', {'matters': matters})

def matter_detail(request, pk):
    matter = get_object_or_404(Matter, pk=pk)
    return render(request, 'eFile/matter_detail.html', {'matter': matter})

def matter_add(request):
    if request.method == 'POST':
        form = MatterForm(request.POST)
        if form.is_valid():
            matter = form.save()
            return redirect('matter_detail', pk=matter.pk)
    else:
        form = MatterForm()
    return render(request, 'eFile/matter_add.html', {'form': form})

def matter_edit(request, pk):
    matter = get_object_or_404(Matter, pk=pk)
    if request.method == 'POST':
        form = MatterForm(request.POST, instance=matter)
        if form.is_valid():
            matter = form.save()
            return redirect('matter_detail', pk=matter.pk)
    else:
        form = MatterForm(instance=matter)
    return render(request, 'eFile/matter_edit.html', {'form': form, 'matter': matter})

def matter_delete(request, pk):
    matter = get_object_or_404(Matter, pk=pk)
    if request.method == 'POST':
        matter.delete()
        return redirect('matter_list')
    return render(request, 'eFile/matter_delete.html', {'matter': matter})


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

