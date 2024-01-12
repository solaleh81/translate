# # views.py
# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from .forms import SignupForm
#
# def home(request):
#     return render(request, 'account/index.html')
#
# def signup(request):
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             confirm_password = form.cleaned_data['confirm_password']
#
#             # Perform any additional validation here
#
#             # Create user if everything is valid
#             user = User.objects.create_user(username, password=password)
#             form.save()
#             # You can customize this part based on your user model
#
#             # Redirect to a success page or login page
#             return redirect('home')  # Change 'login' to your login page URL name
#     else:
#         form = SignupForm()
#
#     return render(request, 'account/signup.html', {'form': form})
