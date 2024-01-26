# views.py
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm


def home(request):
    return render(request, "account/index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
    return render(request, "account/login.html")


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect("home")


# def signup(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             if username:
#                 messages.add_message(request, messages.ERROR, 'نام کاربری وجود دارد.')
#             # elif username == '':
#             #     messages.add_message(request, messages.ERROR, 'نام کاربری را وارد کنید')
#             # elif not username:
#             #     messages.add_message(request, messages.ERROR, 'نام کاربری وجود ندارد.')
#             else:
#                 user = form.save()
#                 login(request, user)
#                 messages.add_message(request, messages.SUCCESS, 'ثبت نام با موفقیت انجام شد.')
#                 # return redirect('home')
#         else:
#             print(form.errors)
#
#
#     else:
#         form = UserCreationForm()
#
#     return render(request, 'account/signup.html', {'form': form})


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password1 = form.cleaned_data["password1"]
            password2 = form.cleaned_data["password2"]
            user = form.save()
            login(request, user)
            messages.add_message(
                request, messages.SUCCESS, "ثبت نام با موفقیت انجام شد."
            )
            # if username:
            #     messages.add_message(request, messages.ERROR, 'نام کاربری وجود دارد.')
            # elif username == '':
            #     messages.add_message(request, messages.ERROR, 'نام کاربری را وارد کنید')
            # elif not username:
            #     messages.add_message(request, messages.ERROR, 'نام کاربری وجود ندارد.')
            if password1 and password2 and password1 != password2:
                messages.add_message(
                    request, messages.ERROR, "رمز اول با رمز دوم برابر نیست!!!!"
                )

        else:
            messages.add_message(
                request,
                messages.ERROR,
                "متاسفانه ثبت نام انجام نشد. مجددا امتحان کنید.",
            )
            print(form.errors)
            # return redirect('home')
        # else:
        #     print(form.errors)

    else:
        form = UserCreationForm()

    return render(request, "account/signup.html", {"form": form})
