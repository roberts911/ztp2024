from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CollaboratorForm
from .models import Collaborator
import uuid

def apply(request):
    if request.method == 'POST':
        form = CollaboratorForm(request.POST)
        if form.is_valid():
            collaborator = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = User.objects.create_user(username=username, password=password)
            collaborator.user = user
            collaborator.save()
            return redirect('status')
    else:
        form = CollaboratorForm()
    return render(request, 'accounts/apply.html', {'form': form})

@login_required
def status(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.is_staff:
        collaborators = Collaborator.objects.all()
    else:
        collaborators = Collaborator.objects.filter(user=request.user)
    return render(request, 'accounts/status.html', {'collaborators': collaborators})

@login_required
def approve(request, nip):
    if not request.user.is_staff:
        return redirect('status')
    collaborator = Collaborator.objects.get(nip=nip)
    collaborator.status = 'Approved'
    collaborator.api_key = uuid.uuid4()
    collaborator.save()
    return redirect('status')

@login_required
def api_key(request):
    collaborator = Collaborator.objects.get(user=request.user)
    if collaborator.status != 'Approved':
        return redirect('status')
    return render(request, 'accounts/api_key.html', {'collaborator': collaborator})