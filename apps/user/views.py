from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password
from .forms import UserForm, LoginForm
from .models import User
from .decorator import login_required

# Create your views here.
def home(request):
    return render(request, 'home.html')

def sign_up(request):
    if request.method == "POST":
        form = UserForm(
            request.POST,
            request.FILES
        )
          

        if form.is_valid():
                user = form.save(commit=False)
                user.password = make_password(form.cleaned_data['password'])
            
                user.save()

                messages.success(
                request, 'You have successfully created your account!'
                )
                return redirect('login')
    else:
        form = UserForm()
    context = {
        'form': form
    }
    return render(request, 'sign_up.html', context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(
            request.POST
        )
        
        if form.is_valid():
            email = form.cleaned_data['email']
            password =form.cleaned_data['password']

            try:
                user = User.objects.get(email=email)

                if check_password(password = user.password):
                    request.session['user_id'] = user.pk
                    request.session['username'] = user.username
                    request.session['user_type'] = user.user_type

                    user.created_at = timezone.now()
                    user.save()

                    messages.success(
                        request, 'Login successful'

                    )
                    return redirect('dashboard')
                else:
                    raise ValueError(
                        'Invalid password, please try again with the correct password'
                    )
            except User.DoesNotExist:
                messages.error(
                    request, '404 User not found!'
                )
    else:
        form = LoginForm()
    
    context = {
        'form': form
    }
    return render(request, "login.html", context)
      
