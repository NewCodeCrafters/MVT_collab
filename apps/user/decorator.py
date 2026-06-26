from django.shortcuts import redirect
from django.contrib import messages
from functools import wraps

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            messages.error(
                request, "Kindly login your account"
            )

            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

def vendor_admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if request.user.user_type not in ["Vendor", "admin"]:
            messages.error(
                request, "You do not have permission to access this page.   "
            )
            return redirect("p_list")
        return view_func(request, *args, **kwargs)
    return wrapper
        


