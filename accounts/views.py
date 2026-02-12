from django.shortcuts import render
from accounts.views import UserCreateForm

# Create your views here.

def register_view(request):
    user_form = UserCreateForm()
    return render(request, 'register.html', {'user_form': user_form})