from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, register
from accounts.forms import LoginForm, UserRegisterForm


def sign_in(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data["username"], password=data["password"])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Signed in successfully")
                else:
                    return HttpResponse("Account is disabled")
            else:
                return HttpResponse("Wrong user data")
        else:
            form = LoginForm()
    else:
        form = LoginForm()
    return render(request, 'login.html', context={"form": form})


def logout_user(request):
    logout(request)
    return HttpResponse("You logged out successfully")


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user':new_user})
    else:
        user_form = UserRegisterForm()
    return render(request, 'register.html', {'user_form': user_form})
