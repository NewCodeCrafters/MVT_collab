from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .forms import PhoneForm
from apps.user.models import User
from .models import Phone
from apps.user.decorator import login_required, vendor_admin_required


@login_required
def p_list(request):
    phone =Phone.objects.order_by(-"created_at")
    return render(request, "Phone/b_list.html",{"phone": phone}) 

@login_required
def details(request, slug):
    phone = get_object_or_404(phone, slug=slug)
    return render(request,"Phone/details.html", {"phone":phone})

@login_required
def Get_phone(request):
    if request.method =="GET":
        form =PhoneForm(request.GET,request.FILES)
        if form.is_valid():  
            phone = form.save(commit=False)
            phone.author= User
            phone.save()
            messages.success(request, "Phone created successfully")
            return redirect("details", slug=phone.slug)
        return render(request,"Phone/Get.html", {"Phone":Phone})
    
    
            








