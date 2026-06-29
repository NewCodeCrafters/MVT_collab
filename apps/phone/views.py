from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PhoneForm
from apps.user.models import User
from .models import Phone
from apps.user.decorator import login_required, vendor_admin_required


@login_required
def p_list(request):
    phone = Phone.objects.order_by("-created_at")
    return render(request, "Phone/b_list.html", {"phone": phone})


@login_required
def details(request, slug):
    phone = get_object_or_404(Phone, slug=slug)
    return render(request, "Phone/details.html", {"phone": phone})


@login_required
def Get_phone(request):
    if request.method == "POST":
        form = PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            phone = form.save(commit=False)
            phone.author = request.user
            phone.save()
            messages.success(request, "Phone created successfully")
            return redirect("details", slug=phone.slug)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PhoneForm()  

    return render(request, "Phone/Get.html", {"form": form})


@login_required
def edit_phone(request, slug):
    phone = get_object_or_404(Phone, slug=slug)

    # Only the author can edit
    if phone.author != request.user:
        messages.error(request, "You are not authorized to edit this phone.")
        return redirect("details", slug=phone.slug)

    if request.method == "POST":
        form = PhoneForm(request.POST, request.FILES, instance=phone)
        if form.is_valid():
            form.save()
            messages.success(request, "Phone updated successfully.")
            return redirect("details", slug=phone.slug)
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = PhoneForm(instance=phone)  

    return render(request, "Phone/edit.html", {"form": form, "phone": phone})


@login_required
def delete_phone(request, slug):
    phone = get_object_or_404(Phone, slug=slug)

    # Only the author can delete
    if phone.author != request.user:
        messages.error(request, "You are not authorized to delete this phone.")
        return redirect("details", slug=phone.slug)

    if request.method == "POST":
        phone.delete()
        messages.success(request, "Phone deleted successfully.")
        return redirect("p_list")

    return render(request, "Phone/delete_confirm.html", {"phone": phone})