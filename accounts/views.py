from django.shortcuts import redirect, render
from accounts.views import UserCreateForm, AuthenticationForm

# Create your views here.

def register_view(request):
    if request.method == "POST":
        user_form = UserCreateForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('login')
        
    else:
        user_form = UserCreateForm()
    return render(request, 'register.html', {'user_form': user_form})

def login_view(request):
    login_form = AuthenticationForm()
    return render(request, 'login.hmtl', {'login_form': login_form})
