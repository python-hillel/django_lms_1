from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from groups.forms import GroupCreateForm, GroupUpdateFrom
from groups.models import Group
from students.models import Student


def get_groups(request):
    groups = Group.objects.all()
    return render(request, 'group/list.html', {'groups': groups})


def create_group(request):
    if request.method == 'POST':
        form = GroupCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))
    elif request.method == 'GET':
        form = GroupCreateForm()
        return render(request, 'group/create.html', {'form': form})


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    students = {'students': Student.objects.filter(group=group)}
    if request.method == 'POST':
        form = GroupUpdateFrom(data=request.POST, instance=group, initial=students)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    form = GroupUpdateFrom(instance=group, initial=students)
    return render(request, 'group/update.html', {'form': form, 'group': group})


def detail_group(request, pk):
    return HttpResponse(f'DETAIL GROUP VIEW for group {pk}')


def delete_group(request, pk):
    return HttpResponse(f'DELETE GROUP VIEW for group {pk}')
