from django.shortcuts import render , redirect
from .forms import UserCreationForms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate ,login , logout
# Create your views here.
def signup_view(request):
    if request.method =='POST':
        form = UserCreationForms(request.POST)
        if form.is_valid():
            messages.success(request , 'Account created successfully')
            form.save()
            return redirect('signup')
    else:
        form = UserCreationForms()
    return render(request, 'signup.html', {'form':form})
def login_view(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request , data = request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data['password']
                user = authenticate(username = username, password = password)
                if user is not None:
                    login(request,user)
                    messages.success(request , 'Loged In successfully')
                    return redirect('profile')
                else:
                    messages.success(request , 'LogeIn information incorrect')
                    return redirect('signup')
        else:
            form = AuthenticationForm()
    return render(request, 'signup.html',{'form':form})

def profile_view(request):
    return render(request, 'profile.html')

def logout_view(request):
    logout(request)
    return redirect("login")