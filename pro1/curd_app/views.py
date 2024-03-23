from django.shortcuts import render, redirect
from .forms import CollegeForm
from .models import College
from django.http import HttpResponse


def create_view(request):
    template_name = "curd_app/create.html"
    form = CollegeForm()
    if request.method == "POST":
        form = CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("data saved")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    template_name = "curd_app/show.html"
    obj = College.objects.all()
    context = {"obj": obj}
    return render(request, template_name, context)


def update_view(request, pk):
    template_name = "curd_app/create.html"
    obj = College.objects.all()
    form = CollegeForm(instance=obj)
    if request.method == "POST":
        form = CollegeForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def cancel_view(request, pk):
    template_name = "curd_app/confirm.html"
    obj = College.objects.get(id=pk)
    form = CollegeForm(instance=obj)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, template_name)